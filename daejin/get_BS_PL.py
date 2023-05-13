import csv

#keys: '종목코드'		num
#		'회사명',		str
#		'시장구분',		str
#		'업종',			str
#		'업종명',		str
# 		'결산월',		num
# 		'결산기준일',	str
# 		'보고서종류',	str
# 		'통화',			str
# 		'항목코드',		str
# 		'항목명',		str
# 		'당기',			num
# 		'전기',			num
# 		'전전기',		num
# 		'재무제표종류'	str

#재무제표종류 키 값이 \ufeff가 앞에 붙어 오염되는 것을 확인하여 pop으로 제거 후 다시 추가하였고, 종목코드의 []를 제거하였고, 단위를 통일하기 위해 ,를 제거하였습니다.
def cleanse_data(row):
	row['재무제표종류'] = row.pop('\ufeff재무제표종류')
	row['종목코드'] = row['종목코드'].replace('[', '').replace(']', '')
	row['당기'] = row['당기'].replace(',', '')
	row['전기'] = row['전기'].replace(',', '')
	row['전전기'] = row['전전기'].replace(',', '')

def get_BS():
	num_val_lst = ['종목코드', '결산월', '당기', '전기', '전전기']
	f = open('./data/2022/별도재무상태표_2022.csv', 'rt', encoding='UTF8')
	BS = []
	reader = csv.DictReader(f)
	for row in reader:
		cleanse_data(row)
		for item in row:
			if item in num_val_lst and row[item] != '':
				row[item] = int(row[item])
		BS.append(row)
		print(row)
	f.close()
	return BS

def get_PL():
	f = open('./data/2022/손익계산서_2022.csv', 'rt', encoding='UTF8')
	PL = []
	reader = csv.DictReader(f)
	for row in reader:
		cleanse_data(row)
		PL.append(row)
	f.close()
	return PL

#재무상태표와 손익계산서 데이터를 가져왔습니다. 저장 형식은 딕셔너리 리스트입니다.
BS = get_BS()
print(BS[0].keys())
for i in range(10):
	print(BS[i])
PL = get_PL()
for i in range(10):
	print(PL[i])
