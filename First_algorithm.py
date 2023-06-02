#1. 시가총액 >= 500000000000 or 매출액 >= 1000000000000
#2. 시가총액/당기순이익 <= 13 or 시가총액/당기순이익 * 시가총액/자본총계 <= 20
#3. 유동자산/유동부채 >= 1.5
#4. 당기순이익/자본총계 >= 0.15

from get_BS_PL import *
from get_sync_data import *

def firstarg1_point(cap, sales, per, tcap, lasset, lliability, income):
    corp = []
    debtr = lasset / lliability
    roe = income / tcap
    if cap >= 500000000000 or sales >= 1000000000000:
        if per <= 13 or per * cap/tcap <= 20:
            if debtr >= 1.5:
                if income / tcap >= 0.15:
                    cap /= 1000000000000
                    x, y, z, w = 4, 3, 2, 6
                    if cap > 100:
                        cap = 100
                    if per < 1:
                        per = 1
                    if debtr > 10:
                        debtr = 10
                    if roe > 0.3:
                        roe = 0.3
                    CAP = round(50/99.5 * cap + 50 - 25/99.5, 2)
                    PER = round(-25/6 * per + 100 + 25/6, 2)
                    DEBTR = round(50/8.5 * debtr + 50 - 150/17 ,2)
                    ROE = round(1000/3 * roe ,2)
                    corp = [CAP, PER, DEBTR, ROE, round((x*cap+y*PER+z*DEBTR+w*ROE)/(x+y+z+w), 2)]
                    return corp
    return

def firstarg2_point(cap, sales, per, tcap, lasset, lliability, income):
    corp = []
    debtr = lasset / lliability
    roe = income / tcap
    if cap >= 300000000000 or sales >= 800000000000:
            if per <= 13 or per * cap/tcap <= 20:
                if debtr >= 1.5:
                    if income / tcap >= 0.2:
                        cap /= 1000000000000
                        x, y, z, w = 4, 3, 2, 6
                        if cap > 100:
                            cap = 100
                        if per < 1:
                            per = 1
                        if debtr > 10:
                            debtr = 10
                        if roe > 0.5:
                            roe = 0.5
                        CAP = round(50/99.7 * cap + 50 - 15/99.7,2)
                        PER = round(-25/6 * per + 100 + 25/6, 2)
                        DEBTR = round(50/8.5 * debtr + 50 - 150/17 ,2)
                        ROE = round(500/3 * roe + 50 - 100/3, 2)
                        corp = [CAP, PER, DEBTR, ROE, round((x*CAP+y*PER+z*DEBTR+w*ROE)/(x+y+z+w), 2)]
                        return corp
    return

OUTLAW_LIST = []

def first_arg(choice=1):
	arg_corp = {}
	for key in MERGED_REPORT:
		company = key
	
		CAP = get_market_cap(company)
		
		if CAP == NOT_EXISTING:
			continue
		CAP = float(CAP.replace(',', '')) * 100000000
	
		try:
			NET_INCOME = get_dangi(company, "당기순이익")
			per = CAP / NET_INCOME
			try:   
				sales = int(get_dangi(company, "매출액"))
			except:
				sales = int(get_dangi(company, "매출"))
			tcap = get_dangi(company, "자본총계")
			lasset = int(get_dangi(company, "유동자산"))
			lliability = int(get_dangi(company, "유동부채"))
			corp = []
			if sales==None: continue
			if tcap==None: continue
			if choice==1:corp = firstarg1_point(CAP, sales, per, tcap, lasset, lliability, NET_INCOME)
			elif choice==2 : corp = firstarg2_point(CAP, sales, per, tcap, lasset, lliability, NET_INCOME)
			if corp != None : arg_corp[company] = corp  
		except:
			OUTLAW_LIST.append(company)
			continue
	return arg_corp

print(first_arg())
print(OUTLAW_LIST)

'''
  if cap >= 300000000000 or sales >= 800000000000:
        if per <= 13 or per * cap/tcap <= 20:
            if debtr >= 1.5:
                if income / tcap >= 0.2:
                    cap /= 1000000000000
                    x, y, z, w = 6, 3, 2, 5
                    if cap > 100:
                        cap = 100
                    if per < 1:
                        per = 1
                    if debtr > 10:
                        debtr = 10
                    if roe > 0.5:
                        roe = 0.5
                    CAP = round(50/99.7 * cap + 50 - 15/99.7,2)
                    PER = round(-25/6 * per + 100 + 25/6, 2)
                    DEBTR = round(50/8.5 * debtr + 50 - 150/17 ,2)
                    ROE = round(500/3 * roe + 50 - 100/3, 2)
                    corp = [CAP, PER, DEBTR, ROE, round((x*CAP+y*PER+z*DEBTR+w*ROE)/(x+y+z+w), 2)]
                    return corp
    if cap >= 300000000000 or sales >= 800000000000:
        if per <= 13 or per * cap/tcap <= 20:
            if debtr >= 1.5:
                if income / tcap >= 0.2:
                    cap /= 1000000000000
                    x, y, z, w = 6, 3, 2, 5
                    if cap > 100:
                        cap = 100
                    if per < 1:
                        per = 1
                    if debtr > 10:
                        debtr = 10
                    if roe > 0.5:
                        roe = 0.5
                    CAP = round(50/99.7 * cap + 50 - 15/99.7,2)
                    PER = round(-25/6 * per + 100 + 25/6, 2)
                    DEBTR = round(50/8.5 * debtr + 50 - 150/17 ,2)
                    ROE = round(500/3 * roe + 50 - 100/3, 2)
                    corp = [CAP, PER, DEBTR, ROE, round((x*CAP+y*PER+z*DEBTR+w*ROE)/(x+y+z+w), 2)]
                    return corp
'''