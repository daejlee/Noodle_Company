#1. 시가총액 >= 500000000000 or 매출액 >= 1000000000000
#2. 시가총액/당기순이익 <= 13 or 시가총액/당기순이익 * 시가종액/자본총계 <= 20
#3. 유동자산/유동부채 >= 1.5
#4. 당기순이익/자본총계 >= 0.15
#5. EPS 7년 성장률 >= 1.11

BS = get_BS()
ticker_list = []  # 조건을 만족하는 기업 저장할 리스트

for data in BS:
    # 조건 1: 시가총액 >= 500000000000 or 매출액 >= 1000000000000
    if data['시가총액'] >= 500000000000 or data['매출액'] >= 1000000000000:

        # 조건 2: 시가총액/당기순이익 <= 13 or 시가총액/당기순이익 * 시가종액/자본총계 <= 20
        if (data['시가총액'] / data['당기순이익'] <= 13) or (data['시가총액'] / data['당기순이익'] * data['시가종가'] / data['자본총계'] <= 20):

            # 조건 3: 유동자산/유동부채 >= 1.5
            if data['유동자산'] / data['유동부채'] >= 1.5:

                # 조건 4: 당기순이익/자본총계 >= 0.15
                if data['당기순이익'] / data['자본총계'] >= 0.15:

                    # 조건 5: EPS 7년 성장률 >= 1.11
                    if data['EPS 7년 성장률'] >= 1.11:
                        ticker_list.append(data['티커'])

print(ticker_list)  # 조건을 만족하는 기업 출력


"""from db import MERGED_REPORT
def	get_dangi(company_name, search_value):
	for item in MERGED_REPORT[company_name]:
		if item['항목명'] == search_value:
			return item["당기"]
def filter_condition_1(company_name):
    market_cap = get_dangi(company_name, '시가총액')
    revenue = get_dangi(company_name, '매출액')
    if market_cap >= 500000000000 or revenue >= 1000000000000:
        return True
    return False

# 2. 시가총액/당기순이익 <= 13 or 시가총액/당기순이익 * 시가종액/자본총계 <= 20
def filter_condition_2(company_name):
    market_cap = get_dangi(company_name, '시가총액')
    net_profit = get_dangi(company_name, '당기순이익')
    total_assets = get_dangi(company_name, '자본총계')
    if market_cap / net_profit <= 13 or market_cap / net_profit * market_cap / total_assets <= 20:
        return True
    return False

# 3. 유동자산/유동부채 >= 1.5
def filter_condition_3(company_name):
    current_assets = get_dangi(company_name, '유동자산')
    current_liabilities = get_dangi(company_name, '유동부채')
    if current_assets / current_liabilities >= 1.5:
        return True
    return False

# 4. 당기순이익/자본총계 >= 0.15
def filter_condition_4(company_name):
    net_profit = get_dangi(company_name, '당기순이익')
    total_equity = get_dangi(company_name, '자본총계')
    if net_profit / total_equity >= 0.15:
        return True
    return False

# 조건에 맞는 기업 찾기
def find_companies():
    filtered_companies = []
    for company_name in MERGED_REPORT.keys():
        if (
            filter_condition_1(company_name) and
            filter_condition_2(company_name) and
            filter_condition_3(company_name) and
            filter_condition_4(company_name)
        ):
            filtered_companies.append(company_name)
    return filtered_companies

# 조건에 맞는 기업 찾기
filtered_companies = find_companies()

# 결과 출력
for company_name in filtered_companies:
    print(company_name)"""


"""def filter_companies(report):
    filtered_companies = {}
    for company, data in report.items():
        # 조건 1: 시가총액 >= 500000000000 or 매출액 >= 1000000000000
        if data[0]['시가총액'] >= 500000000000 or data[0]['매출액'] >= 1000000000000:
            # 조건 2: 시가총액/당기순이익 <= 13 or 시가총액/당기순이익 * 시가종액/자본총계 <= 20
            if (data[0]['시가총액'] / data[0]['당기순이익'] <= 13) or (
                    data[0]['시가총액'] / data[0]['당기순이익'] * data[0]['시가종액'] / data[0]['자본총계'] <= 20):
                # 조건 3: 유동자산/유동부채 >= 1.5
                if data[0]['유동자산'] / data[0]['유동부채'] >= 1.5:
                    # 조건 4: 당기순이익/자본총계 >= 0.15
                    if data[0]['당기순이익'] / data[0]['자본총계'] >= 0.15:
                        filtered_companies[company] = data

    return filtered_companies


# MERGED_REPORT에서 필터링을 수행하여 조건에 맞는 기업들을 얻습니다.
filtered_companies = filter_companies(MERGED_REPORT)

# 결과 출력
for company, data in filtered_companies.items():
    print("회사명:", company)
    print("데이터:", data)
    print("---")"""
