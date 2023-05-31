from get_sync_data import get_KOSPI

Kospi = float(get_KOSPI().replace(',', ''))

BI = 0.79 * Kospi / 2150 * 100

stk = 0

if BI < 91:
    stk = -10 / 34 * (BI-91) + 70
    if stk > 80:
        stk = 80
else:
    stk = -0.1865 * (BI-91) * (BI-93.6) + 70
    if stk < 30:
        stk = 30

Mk_stat = 0

if BI <= 60:
     Mk_stat = 1
elif BI <= 77:
    Mk_stat = 2
elif BI <= 95:
    Mk_stat = 3
elif BI <= 112:
    Mk_stat = 4
else: Mk_stat = 5
