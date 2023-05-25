import numpy as np
import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

def get_price(ticker, start_date=None, end_date=None):
    end_date = end_date if end_date else datetime.today().strftime('%Y-%m-%d')
    start_date = start_date if start_date else (datetime.today() - relativedelta(months=12)).strftime('%Y-%m-%d')
    df = yf.download(ticker, start=start_date, end=end_date)
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
        df.loc[r, 'au'] = (df.loc[r-1, 'au']*(w-1) + df.loc[r, 'diff'] if df.loc[r, 'diff']>0 else 0) / w
        df.loc[r, 'ad'] = (df.loc[r-1, 'ad']*(w-1) + np.abs(df.loc[r, 'diff']) if df.loc[r, 'diff']<0 else 0) / w
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

# x축을 공유하는 subplot으로 겹쳐 그리기 (좌우에 각각 y축 설정)
def draw_chart(df, left: list = None, right: list = None, bottom: str = None):
    fig, ax1 = plt.subplots()
    x = df.index
    # left
    if left:
        for col in left:
            ax1.plot(x, df[col], label=col)
    else:
        # left가 없다면 y축 안 보이도록 설정 (안 해줄 경우 0~1로 나타남)
        ax1.yaxis.set_visible(False)

    # right
    if right:
        # right가 있을 경우 left 눈금선은 생략
        ax1.grid(False, axis='y')
        ax2 = ax1.twinx()
        # left와 색상 안 겹치도록
        ax2._get_lines.prop_cycler = ax1._get_lines.prop_cycler
        for col in right:
            ax2.plot(x, df[col], label=col)

    # bottom
    if bottom:
        ax3 = ax1.twinx()
        ax3.fill_between(x, 0, df[bottom], color='red', alpha=.5)
        ax3.set_ylim(0, 10)
        ax3.axes.yaxis.set_visible(False)

    fig.legend()


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
df_prices = get_price('AAPL', '2023-01-01', '2023-05-19')

# 인덱스 재설정
df_prices.reset_index(drop=True, inplace=True)

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

# MACD 차트 그리기
print("MACD:")
print(df_macd)
draw_chart(df_macd, left=['macd', 'macd_signal'], bottom='macd_oscillator')
plt.show()

# MACD에 기반한 거래 신호 생성
df_macd_signals = indicator_to_signal(df_macd, 'macd_oscillator', 0, 0)
print("MACD Signals:")
print(df_macd_signals)

# RSI 차트 그리기
print("RSI:")
print(df_rsi)
draw_chart(df_rsi, left=['rsi'])
plt.show()

# Envelope 차트 그리기
print("Envelope:")
print(df_envelope)
draw_chart(df_envelope, left=['Close', 'ub', 'lb'])
plt.show()

# Bollinger 차트 그리기
print("Bollinger:")
print(df_bollinger)
draw_chart(df_bollinger, left=['Close', 'ub', 'lb'])
plt.show()

# Bollinger Bands에 기반한 거래 신호 생성
df_bollinger_signals = band_to_signal(df_bollinger, 'A', 'B')
print("Bollinger Bands Signals:")
print(df_bollinger_signals)

# Stochastic 차트 그리기
print("Stochastic:")
print(df_stochastic)
draw_chart(df_stochastic, left=['slow_k', 'slow_d'])
plt.show()

#수장함