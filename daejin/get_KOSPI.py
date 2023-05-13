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

print(get_KOSPI())