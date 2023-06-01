'''
1. 소외된 대형주에 투자
    1. KOSPI 시가 총액 상위 200개 기업
    2. PER이 가장 낮은 6~10개 기업 = NLC
    3. 다른 정량 요건 추가
2. 염가 종목 매수 
    13. NCAV / 시가총액 > 100%
    2. 내재가치 평가 → 7년 평균 이익 20배 이하로 대체??
3. 주가 지수가 낮을 때 (mk_stat≤2)
4. 부채비율 ≤ 150%, 시가총액 > 2천억
'''

from get_BS_PL import *
from get_sync_data import *
from Buffett import *

def kosper200():
    NLC = {}
    KOSPI200_PER = {}
    for company in KOSPI_200:
        for key in MERGED_REPORT:
            if key==company:
                CAP = get_market_cap(company)
                if CAP == NOT_EXISTING:
                    continue
                CAP = float(CAP.replace(',', '')) * 100000000
            try:
                NET_INCOME = round(get_dangi(company, "당기순이익"), 3)
                per = round(CAP / NET_INCOME, 3)
            except:
                continue
            KOSPI200_PER[company] = per
            
    sorted_kosper200 = sorted(KOSPI200_PER.items(), key=lambda x: x[1])
    a = 0
    for k,v in sorted_kosper200:
        if v>0:
            NLC[k] = v
            a +=1
        if a==20:
            break
    return NLC

def thirdarg4(ncav, cap, debtr, per,):
    corp = []
    ncavr = ncav / cap
    if per > 0:
        if debtr <=1.5:
            x, y, z = 5, 2, 3
            if ncavr >= 5:
                ncavr = 5
            elif ncavr <=0:
                ncavr = 0
            if debtr <= 0:
                debtr = 0
            if per <= 1:
                per = 1
            NCAVR = round(100/7 * (ncavr) + 200/7, 2)
            DEBTR = round(-100 * debtr + 100, 2)
            PER =  round(-50/9 * per + 50/9 + 100, 2)
            corp = [NCAVR, DEBTR, PER, round((x*NCAVR+y*DEBTR+z*PER)/(x+y+z), 2)]
            return corp
    return

def thirdarg5(ncav, cap, debtr, per,):
    corp = []
    ncavr = ncav / cap
    if ncavr > 0.5:
        if debtr <= 1:
            x, y, z = 5, 2, 3
            if ncavr >= 5:
                ncavr = 5
            elif ncavr <=0:
                ncavr = 0
            if debtr <= 0:
                debtr = 0
            if per <= 1:
                per = 1
            NCAVR = round(100/7 * (ncavr) + 200/7, 2)
            DEBTR = round(-100 * debtr + 100, 2)
            PER =  round(-50/9 * per + 50/9 + 100, 2)
            corp = [NCAVR, DEBTR, PER, round((x*NCAVR+y*DEBTR+z*PER)/(x+y+z), 2)]
            return corp
    return

NLC = kosper200()     
OUTLAW_LIST = []

def third_arg(choice=4):        
    Thirdarg_corp = {}
    for key in NLC:
        company = key
    
        CAP = get_market_cap(company)
        
        if CAP == NOT_EXISTING:
            continue
        CAP = float(CAP.replace(',', '')) * 100000000
    
        try:
            NET_INCOME = round(get_dangi(company, "당기순이익"), 3)
            ncav = get_dangi(company, "유동자산") - get_dangi(company, "부채총계")
            per = round(CAP / NET_INCOME, 3)
            debtr = get_dangi(company, "부채총계") / get_dangi(company, "자본총계")
        except:
            OUTLAW_LIST.append(company)
            continue
        
        if choice==4 : corp = thirdarg4(ncav, CAP, debtr, per,)
        elif choice==5 : corp = thirdarg5(ncav, CAP, debtr, per,)
        
        if corp != None: Thirdarg_corp[company] = corp

    return Thirdarg_corp
        
print(third_arg(5))
