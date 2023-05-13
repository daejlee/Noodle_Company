import csv

def get_BS():
	f = open('./data/2022/별도재무상태표_2022.csv', 'rt', encoding='UTF8')
	BS = []
	reader = csv.DictReader(f)
	#재무제표종류 키 값이 \ufeff가 앞에 붙어 오염되는 것을 확인하여 pop으로 제거 후 다시 추가하였습니다.
	for row in reader:
		row['재무제표종류'] = row.pop('\ufeff재무제표종류')
		BS.append(row)
	f.close()
	return BS

def get_PL():
	f = open('./data/2022/손익계산서_2022.csv', 'rt', encoding='UTF8')
	PL = []
	reader = csv.DictReader(f)
	#재무제표종류 키 값이 \ufeff가 앞에 붙어 오염되는 것을 확인하여 pop으로 제거 후 다시 추가하였습니다.
	for row in reader:
		row['재무제표종류'] = row.pop('\ufeff재무제표종류')
		PL.append(row)
	f.close()
	return PL

#재무상태표와 손익계산서 데이터를 가져왔습니다. 저장 형식은 딕셔너리 리스트입니다.
BS = get_BS()
for i in range(10):
	print(BS[i])
PL = get_PL()
for i in range(10):
	print(PL[i])

#살펴본 결과 모든 value가 str타입이네요.. 종목코드나 업종, 전기, 전전기 등은 숫자 자료형으로 바꿔주는 게 나을 것 같아욥.