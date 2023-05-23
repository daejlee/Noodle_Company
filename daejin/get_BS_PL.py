import csv

#필요없는 키들을 삭제했고, 종목코드의 []를 제거하였고, 단위를 통일하기 위해 당기, 전기, 전전기의 ,를 제거하였습니다.
def cleanse_data(row):
	del(row['\ufeff재무제표종류'])
	del(row['시장구분'])
	del(row['업종'])
	del(row['업종명'])
	del(row['결산월'])
	del(row['결산기준일'])
	del(row['보고서종류'])
	del(row['통화'])
	del(row['항목코드'])
	row['종목코드'] = row['종목코드'].replace('[', '').replace(']', '')
	row['당기'] = row['당기'].replace(',', '')
	row['전기'] = row['전기'].replace(',', '')
	row['전전기'] = row['전전기'].replace(',', '')
	num_val_lst = ['종목코드', '당기', '전기', '전전기']
	for item in row:
		if item in num_val_lst and row[item] != '':
			row[item] = int(row[item])
	return row

def get_BS():
	#파일명은 본인 컴퓨터 환경 따라 다를 수 있습니다. 일단 제 컴퓨터 환경에서의 파일명을 걸어놨어요.
	file_name = "C:/Users/savif/OneDrive/바탕 화면/Noodle_Company/daejin/cache/2022/2022_BS.csv"
	f = open(file_name, 'rt', encoding='UTF8')
	reader = csv.DictReader(f)
	cleansed_data = []
	for row in reader:
		cleansed_data.append(cleanse_data(row))
	BS_2022 = {}
	prev_row = cleansed_data[0]
	lst = []
	for row in cleansed_data:
		if prev_row['회사명'] != row['회사명']:
			BS_2022[prev_row['회사명']] = lst
			lst = []
		prev_row = row
		lst.append(row)
	f.close()
	return BS_2022

def get_PL():
	#파일명은 본인 컴퓨터 환경 따라 다를 수 있습니다. 일단 제 컴퓨터 환경에서의 파일명을 걸어놨어요.
	file_name = "C:/Users/savif/OneDrive/바탕 화면/Noodle_Company/daejin/cache/2022/2022_PL.csv"
	f = open(file_name, 'rt', encoding='UTF8')
	reader = csv.DictReader(f)
	cleansed_data = []
	for row in reader:
		cleansed_data.append(cleanse_data(row))
	PL_2022 = {}
	prev_row = cleansed_data[0]
	lst = []
	for row in cleansed_data:
		if prev_row['회사명'] != row['회사명']:
			PL_2022[prev_row['회사명']] = lst
			lst = []
		prev_row = row
		lst.append(row)
	f.close()
	return PL_2022

def merge_BS_PL(BS, PL):
	ret = {}
	for b_key, b_val in BS.items():
		ret[b_key] = b_val
		for p_key, p_val in PL.items():
			if b_key == p_key:
				for i in range(len(p_val)):
					ret[b_key].append(p_val[i])
					# for k in range(len((p_val)[i])):
	return ret

#재무상태표와 손익계산서 데이터를 가져왔습니다. 저장 형식은 딕셔너리 리스트입니다.
BS = get_BS()
PL = get_PL()

#BS와 PL을 합쳤습니다. BS만 있는 기업은 일단 BS만 넣어놨습니다.
MERGED_REPORT = merge_BS_PL(BS, PL)

#ex) 당기 구하는 함수입니다. get_dangi("경방", "매출액") 이렇게 쓰시면 됩니다. 따옴표 필수!
def	get_dangi(company_name, search_value):
	for item in MERGED_REPORT[company_name]:
		if search_value in item['항목명']:
			return item["당기"]

#사용예시
print(get_dangi("경방", "유동자산"))