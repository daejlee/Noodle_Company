'''
1. NCAV / 시가총액 ≥ 150%
2. 당기순이익 > 0
3. 부채총계 / 자본총계 ≤ 50%
4. PER ≤ 10
'''

from get_BS_PL import *
from get_sync_data import *

def secarg_point(ncav, cap, debtr, per, a=1.5, b=0.5, c=10, d=300000000000):
    corp = []
    ncavr = ncav / cap
    if ncavr >= a:
        if debtr <= b:
            if per <= c and per > 0:
                if cap >= d:
                    x, y, z = 5, 2, 3
                    if ncavr >= 5:
                        ncavr = 5
                    if per <= 1:
                        per = 1
                    NCAVR = round(100/7 * (ncavr) + 200/7, 2)
                    DEBTR = round(-100 * debtr + 100, 2)
                    PER =  round(-50/9 * per + 50/9 + 100, 2)
                    corp = [NCAVR, DEBTR, PER, round((x*NCAVR+y*DEBTR+z*PER)/(x+y+z), 2)]
                    return corp				
    return

OUTLAW_LIST = []

def sec_arg(a=1.5, b=0.5, c=10, d=300000000000):
	secarg_corp = {}
	for key in MERGED_REPORT:
		company = key
		
		CAP = get_market_cap(company)
		
		if CAP == NOT_EXISTING:
			continue
		CAP = float(CAP.replace(',', '')) * 100000000
	
		try:
			ncav = get_dangi(company, "유동자산") - get_dangi(company, "부채총계")
			NET_INCOME = get_dangi(company, "당기순이익")
			per = CAP / NET_INCOME
			debtr = get_dangi(company, "부채총계") / get_dangi(company, "자본총계")
		except:
			OUTLAW_LIST.append(company)
			continue

		corp = secarg_point(ncav, CAP, debtr, per, a, b, c, d)
		if corp != None: secarg_corp[company] = corp
	return secarg_corp

print(sec_arg())