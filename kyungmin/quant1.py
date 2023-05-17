import numpy as np
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_price(ticker, start_date=None, end_date=None):
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else datetime.today().date()
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else end_date - relativedelta(months=12)
    df = web.DataReader(ticker, 'yahoo', start=start_date, end=end_date)
    return df

def macd(df, short=12, long=26, signal=9):
    df['ema_short'] = df['Close'].ewm(span=short).mean()
    df['ema_long'] = df['Close'].ewm(span=long).mean()
    df['macd'] = df['ema_short'] - df['ema_long']
    df['macd_signal'] = df['macd'].ewm(span=signal).mean()
    df['macd_oscillator'] = df['macd'] - df['macd_signal']
    return df

def rsi(df, w=14):
    df['diff'] = df['Close'].diff()
    df['au'] = df['diff'].where(df['diff']>0, 0).rolling(w).mean()
    df['ad'] = df['diff'].where(df['diff']<0, 0).rolling(w).mean().abs()
    for r in range(w+1, len(df)):
        df['au'][r] = ( df['au'][r-1]*(w-1) + df['diff'].where(df['diff']>0,0)[r] ) / w
        df['ad'][r] = ( df['ad'][r-1]*(w-1) + df['diff'].where(df['diff']<0,0).abs()[r] ) / w
    df['rsi'] = df['au'] / (df['au'] + df['ad']) * 100
    return df

def envelope(df, w=50, spread=.05):
    df['center'] = df['Close'].rolling(w).mean()
    df['ub'] = df['center']*(1+spread)
    df['lb'] = df['center']*(1-spread)
    return df

def bollinger(df, w=20, k=2):
    df['center'] = df['Close'].rolling(w).mean()
    df['sigma'] = df['Close'].rolling(w).std()
    df['ub'] = df['center'] + k*df['sigma']
    df['lb'] = df['center'] - k*df['sigma']
    return df

def stochastic(df, n=14, m=3, t=3):
    df['fast_k'] = ( df['Close'] - df['Low'].rolling(n).min() ) / ( df['High'].rolling(n).max() - df['Low'].rolling(n).min() ) * 100
    df['slow_k'] = df['fast_k'].rolling(m).mean()
    df['slow_d'] = df['slow_k'].rolling(t).mean()
    return df


def indicator_to_signal(df, factor, buy, sell):
    df['trade'] = np.nan
    if buy >= sell:
        df['trade'].mask(df[factor] > buy, 'buy', inplace=True)
        df['trade'].mask(df[factor] < sell, 'zero', inplace=True)
    else:
        df['trade'].mask(df[factor] < buy, 'buy', inplace=True)
        df['trade'].mask(df[factor] > sell, 'zero', inplace=True)
    df['trade'].fillna(method='ffill', inplace=True)
    df['trade'].fillna('zero', inplace=True)

    df['position_chart'] = 0
    df['position_chart'].mask(df['trade'] == 'buy', 1, inplace=True)
    return df


def band_to_signal(df, buy, sell):
    df['trade'] = np.nan
    # buy
    if buy == 'A':
        df['trade'].mask(df['Close'] > df['ub'], 'buy', inplace=True)
    elif buy == 'B':
        df['trade'].mask((df['ub'] > df['Close']) & (df['Close'] > df['center']), 'buy', inplace=True)
    elif buy == 'C':
        df['trade'].mask((df['center'] > df['Close']) & (df['Close'] > df['lb']), 'buy', inplace=True)
    elif buy == 'D':
        df['trade'].mask((df['lb'] > df['Close']), 'buy', inplace=True)
    # zero
    if sell == 'A':
        df['trade'].mask(df['Close'] > df['ub'], 'zero', inplace=True)
    elif sell == 'B':
        df['trade'].mask((df['ub'] > df['Close']) & (df['Close'] > df['center']), 'zero', inplace=True)
    elif sell == 'C':
        df['trade'].mask((df['center'] > df['Close']) & (df['Close'] > df['lb']), 'zero', inplace=True)
    elif sell == 'D':
        df['trade'].mask((df['lb'] > df['Close']), 'zero', inplace=True)
    df['trade'].fillna(method='ffill', inplace=True)
    df['trade'].fillna('zero', inplace=True)

    df['position_chart'] = 0
    df['position_chart'].mask(df['trade'] == 'buy', 1, inplace=True)
    return df

# 주식 가격 데이터 가져오기
df_prices = get_price('AAPL', '2023-01-01', '2023-05-01')

# MACD 계산
df_macd = macd(df_prices)

# RSI 계산
df_rsi = rsi(df_prices)

# Envelope 계산
df_envelope = envelope(df_prices)

# Bollinger 계산
df_bollinger = bollinger(df_prices)

# Stochastic 계산
df_stochastic = stochastic(df_prices)
