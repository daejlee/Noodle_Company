import urllib.request
from bs4 import BeautifulSoup
import requests

NOT_EXISTING = -1

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
	for key, val in CAP_DICT.items():
		if key == company_name:
			return val
	#시가총액이 존재하지 않을 시 (네이버 증권에 검색되지 않는 회사입니다.)
	return NOT_EXISTING

#크롤링에 시간이 오래 걸려서 한 번에 코스피 코스닥 시가총액을 모두 불러와서 저장해두고 사용하고자 만든 함수입니다. 반환값은 1차원 딕셔너리 입니다.
def get_market_cap_dict():
	cap_dict = {}
	for i in range(41):
		address = 'https://finance.naver.com/sise/sise_market_sum.naver?sosok=0&page=' + str(i + 1)
		res = requests.get(address)
		soup = BeautifulSoup(res.content.decode('euc-kr'), 'html.parser')
		section = soup.find('tbody')
		items = section.find_all('tr', onmouseover="mouseOver(this)")
		for item in items:
			nums = item.find_all('td', 'number')
			basic_info = item.get_text()
			sinfo = basic_info.split("\n")
			cap_dict[sinfo[2]] = nums[4].get_text()
	for i in range(33):
		address = 'https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page=' + str(i + 1)
		res = requests.get(address)
		soup = BeautifulSoup(res.content.decode('euc-kr'), 'html.parser')
		section = soup.find('tbody')
		items = section.find_all('tr', onmouseover="mouseOver(this)")
		for item in items:
			nums = item.find_all('td', 'number')
			basic_info = item.get_text()
			sinfo = basic_info.split("\n")
			cap_dict[sinfo[2]] = nums[4].get_text()
	return cap_dict

#시가총액이 모두 포함된 단일 딕셔너리입니다. {회사명 : 시가총액}
CAP_DICT = get_market_cap_dict()