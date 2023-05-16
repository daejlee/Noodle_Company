import csv

#keys: '종목코드'		num
#		'회사명',		str
#		'시장구분',		str -> 삭제
#		'업종',			str -> 삭제
#		'업종명',		str -> 삭제
# 		'결산월',		num -> 삭제
# 		'결산기준일',	str -> 삭제
# 		'보고서종류',	str -> 삭제
# 		'통화',			str -> 삭제
# 		'항목코드',		str -> 삭제
# 		'항목명',		str
# 		'당기',			num
# 		'전기',			num
# 		'전전기',		num
# 		'재무제표종류'	str -> 삭제
# 그리고 기업별로 하나로 묶기.

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

#BS는 회사명을 키로 하는 이중 딕셔너리입니다. BS[회사명][항목명] = 값
def get_BS():
	BS = []
	for i in range (7):
		file_name = "./cache/inputyear/inputyear_BS.csv".replace('inputyear', str(2016 + i))
		f = open(file_name, 'rt', encoding='UTF8')
		reader = csv.DictReader(f)
		cleansed_data = []
		for row in reader:
			cleansed_data.append(cleanse_data(row))
		globals()['BS_{}'.format(i)] = {}
		prev_row = cleansed_data[0]
		lst = []
		for row in cleansed_data:
			if prev_row['종목코드'] != row['종목코드']:
				globals()['BS_{}'.format(i)][prev_row['종목코드']] = lst
				lst = []
			prev_row = row
			lst.append(row)
		f.close()
		BS.append(globals()['BS_{}'.format(i)])
	return BS

def get_PL():
	PL = []
	for i in range (7):
		file_name = "./cache/inputyear/inputyear_PL.csv".replace('inputyear', str(2016 + i))
		f = open(file_name, 'rt', encoding='UTF8')
		reader = csv.DictReader(f)
		cleansed_data = []
		for row in reader:
			cleansed_data.append(cleanse_data(row))
		globals()['PL_{}'.format(i)] = {}
		prev_row = cleansed_data[0]
		lst = []
		for row in cleansed_data:
			if prev_row['종목코드'] != row['종목코드']:
				globals()['PL_{}'.format(i)][prev_row['종목코드']] = lst
				lst = []
			prev_row = row
			lst.append(row)
		f.close()
		PL.append(globals()['PL_{}'.format(i)])
	return PL

#재무상태표와 손익계산서 데이터를 가져왔습니다. 저장 형식은 딕셔너리 리스트입니다.
BS = get_BS()
PL = get_PL()
