import csv

FILE_PATH = 'C:/Users/savif/workspace/Noodle_Company/cache/2022'

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
	file_name = FILE_PATH + "/2022_BS.csv"
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

def get_PL_C():
	#파일명은 본인 컴퓨터 환경 따라 다를 수 있습니다. 일단 제 컴퓨터 환경에서의 파일명을 걸어놨어요.
	file_name = FILE_PATH + "/2022_PL_C.csv"
	f = open(file_name, 'rt', encoding='UTF8')
	reader = csv.DictReader(f)
	cleansed_data = []
	for row in reader:
		cleansed_data.append(cleanse_data(row))
	PL_C_2022 = {}
	prev_row = cleansed_data[0]
	lst = []
	for row in cleansed_data:
		if prev_row['회사명'] != row['회사명']:
			PL_C_2022[prev_row['회사명']] = lst
			lst = []
		prev_row = row
		lst.append(row)
	f.close()
	return PL_C_2022

def get_PL():
	#파일명은 본인 컴퓨터 환경 따라 다를 수 있습니다. 일단 제 컴퓨터 환경에서의 파일명을 걸어놨어요.
	file_name = FILE_PATH + "/2022_PL.csv"
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

def merge_BS_PL(BS, PL, PL_C):
	ret = {}
	for b_key, b_val in BS.items():
		ret[b_key] = b_val
		for p_key, p_val in PL.items():
			if b_key == p_key:
				for i in range(len(p_val)):
					ret[b_key].append(p_val[i])
					for pc_key, pc_val in PL_C.items():
						if p_key == pc_key:
							for k in range(len(pc_val)):
								ret[b_key].append(pc_val[k])
	return ret

#ex) 당기 구하는 함수입니다.
def	get_dangi(company_name, search_value):
	if search_value == "당기순이익":
		for item in MERGED_REPORT[company_name]:
			name = item['항목명'].replace(' ', '')
			NET_VAL_LST = [
			'당기의순',
			'당기순',
			"당분기순",
			"당기이익",
			"당기연결",
			"#NAME?"]
			for elem in NET_VAL_LST:
				if elem in name and (item["당기"] != "" and item["당기"] != 0):
					return item["당기"]
	if search_value == "자본총계":
		for item in MERGED_REPORT[company_name]:
			name = item['항목명'].replace(' ', '')
			if "기말" in name or "기말" in name:
				return item["당기"]
	for item in MERGED_REPORT[company_name]:
		name = item['항목명'].replace(' ', '')
		if search_value in name:
			return item["당기"]

BS = get_BS()
PL = get_PL()
PL_C = get_PL_C()
#2022BS,PL이 포함된 자료입니다. 이중 딕셔너리입니다. {회사명(key) : 사업보고서(val이면서 딕셔너리 자체)}
MERGED_REPORT = merge_BS_PL(BS, PL, PL_C)