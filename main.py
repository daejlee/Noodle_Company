from get_BS_PL import *
from get_sync_data import *

#다른 회사들과 재무제표 패턴이 다른 극소수 회사들을 저장해놓을 리스트입니다.
OUTLAW_LIST = []

secarg_corp = []
for key in MERGED_REPORT:
	company = key
	CUR_CMP = MERGED_REPORT[company]
	#시가총액입니다.
	CAP = get_market_cap(company)
	#시가총액이 네이버 증권에 존재하지 않는 기업은 패스했습니다.
	if CAP == NOT_EXISTING:
		continue
	#쉼표를 없애고 실수형으로 저장했습니다.
	CAP = float(CAP.replace(',', '')) * 100000000
	try:
		ncav = get_dangi(company, "유동자산") - get_dangi(company, "부채총계")
		#당기순이익입니다.
		NET_INCOME = get_dangi(company, "당기순이익")
		per = CAP / NET_INCOME
	except:
	#위 과정에서 오류가 발생하는 기업들은 따로 모아놨습니다.
		OUTLAW_LIST.append(company)
		continue
	if ncav / CAP >= 1.5:
		if NET_INCOME > 0:
			if get_dangi(company, "부채총계") / get_dangi(company, "자본총계") <= 0.5:
				if per <= 10:
					secarg_corp.append(company)

print(secarg_corp)
