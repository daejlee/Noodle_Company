#1. 시가총액 >= 500000000000 or 매출액 >= 1000000000000
#2. 시가총액/당기순이익 <= 13 or 시가총액/당기순이익 * 시가총액/자본총계 <= 20
#3. 유동자산/유동부채 >= 1.5
#4. 당기순이익/자본총계 >= 0.15


from get_BS_PL import *
from get_sync_data import *

# 다른 회사들과 재무제표 패턴이 다른 극소수 회사들을 저장해놓을 리스트
OUTLAW_LIST = []

secarg_corp = []
for key in MERGED_REPORT:
    company = key
    # 시가총액을 가져오기.
    CAP = get_market_cap(company)
    # 네이버 증권에 존재하지 않는 기업은 건너뛰기.
    if CAP == NOT_EXISTING or CAP is None:
        continue
    # 시가총액을 쉼표를 없애고 실수형으로 변환합니다.
    CAP = float(CAP.replace(',', '')) * 100000000
    try:
        # 당기순이익을 가져옵니다.
        NET_INCOME = get_dangi(company, "당기순이익")
        # 계산하기 전에 값이 None이 아닌지 확인합니다.
        if NET_INCOME is not None:
            # 시가총액 대비 당기순이익의 비율인 P/E 비율을 계산합니다.
            per = CAP / NET_INCOME
        else:
            # 값이 없는 기업은 OUTLAW_LIST에 추가합니다.
            OUTLAW_LIST.append(company)
            continue
    except:
        # 오류가 발생한 기업은 OUTLAW_LIST에 추가합니다.
        OUTLAW_LIST.append(company)
        continue
    # 조건을 확인합니다.
    if CAP >= 500000000000 or (get_dangi(company, "매출액") is not None and get_dangi(company, "매출액") >= 1000000000000):
        if per <= 13 or per * (CAP / get_dangi(company, "자본총계")) <= 20:
            if get_dangi(company, "유동자산") / get_dangi(company, "유동부채") >= 1.5:
                if NET_INCOME / get_dangi(company, "자본총계") >= 0.15:
                    # 조건에 부합하는 기업을 secarg_corp 리스트에 추가합니다.
                    secarg_corp.append(company)

print(secarg_corp)
#푸쉬했습니다.