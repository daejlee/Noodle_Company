import urllib.request
from bs4 import BeautifulSoup

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

print(get_KOSPI())
print(get_price("005930"))