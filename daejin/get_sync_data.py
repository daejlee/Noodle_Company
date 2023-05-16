import urllib.request
from bs4 import BeautifulSoup
import requests

def get_KOSPI():
	#네이버 금융에서 코스피 지수를 크롤링해옵니다.
	url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
	result = urllib.request.urlopen(url)
	bs_obj = BeautifulSoup(result.read(), "html.parser")
	#코스피 지수를 가져옵니다.
	KOSPI = bs_obj.find("em", {"id":"now_value"}).text
	#코스피 지수를 반환합니다.
	return KOSPI

def get_price(company_code):
	#네이버 금융에서 주식 가격을 크롤링해옵니다.
	url = "https://finance.naver.com/item/main.nhn?code=" + company_code
	result = urllib.request.urlopen(url)
	bs_obj = BeautifulSoup(result.read(), "html.parser")
	#주식 가격을 가져옵니다.
	no_today = bs_obj.find("p", {"class":"no_today"})
	blind = no_today.find("span", {"class":"blind"})
	now_price = blind.text
	#주식 가격을 반환합니다.
	return now_price

#시가총액 반환 함수입니다. 네이버 증권 기반 크롤링인데, 해당 페이지의 모든 종목이 종목명으로 구분되어 있기에 종목명을 이용하여 시가총액을 크롤링해야합니다.
def get_market_cap(company_name):
	for i in range(41):
		address = 'https://finance.naver.com/sise/sise_market_sum.naver?&page=' + str(i + 1)
		res = requests.get(address)
		soup = BeautifulSoup(res.content, 'html.parser')
		section = soup.find('tbody')
		items = section.find_all('tr', onmouseover="mouseOver(this)")
		for item in items:
			basic_info = item.get_text()
			sinfo = basic_info.split("\n")
			if sinfo[2] == company_name:
				return sinfo[15]
	#시가총액을 반환합니다.

print(get_KOSPI())
print(get_price("005930"))
print(get_market_cap("삼성전자"))