# KNU 한국어 감성사전
# 작성자 : 온병원, 박상민, 나철원
# 소속 : 군산대학교 소프트웨어융합공학과 Data Intelligence Lab
# 홈페이지 : dilab.kunsan.ac.kr
# 작성일 : 2018.05.14
# 뜻풀이 데이터 출처 : https://github.com/mrchypark/stdkor
# 신조어 데이터 출처 : https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%9D%B8%ED%84%B0%EB%84%B7_%EC%8B%A0%EC%A1%B0%EC%96%B4_%EB%AA%A9%EB%A1%9D
# 이모티콘 데이터 출처: https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%AA%A8%ED%8B%B0%EC%BD%98
# SentiWordNet_3.0.0_20130122 데이터 출처 : http://sentiwordnet.isti.cnr.it/
# SenticNet-5.0 데이터 출처 : http://sentic.net/
# 감정단어사전0603 데이터 출처 : http://datascience.khu.ac.kr/board/bbs/board.php?bo_table=05_01&wr_id=91 
# 김은영, “국어 감정동사 연구”, 2004.02, 학위논문(박사) - 전남대학교 국어국문학과 대학원


#-*-coding:utf-8-*-

import json

class KnuSL(): #단어 사전 클래스 생성

	def data_list(wordname): #단어 어근, 극성 분석 함수 생성	
		with open('SentiWord_info.json', encoding='utf-8-sig', mode='r') as f: #단어 극성치 사전 파일 읽기 모드로 열기
			data = json.load(f) #json 파일 디코딩
		result = ['None','None'] #단어가 사전에서 검색되지 않을 경우에 반환값, 초기값	
		for i in range(0, len(data)): 
			if data[i]['word'] == wordname: #i번째 단어와 사전을 비교해서 단어가 존재하는지 확인 존재하면 아래 코드 실행
				result.pop() #어근값과 극성치값 삭제
				result.pop()
				result.append(data[i]['word_root']) #데이터 리스트에 어근 추가
				result.append(data[i]['polarity'])	 #데이터 리스트에 극성치값 추가
		
		r_word = result[0] #단어의 어근
		s_word = result[1] #단어의 극성치값
							
		print('어근 : ' + r_word)
		print('극성 : ' + s_word)
		return r_word, s_word

	def sentiment_score(wordname):
		with open('SentiWord_info.json', encoding='utf-8-sig', mode='r') as f: #단어 극성치 사전 파일 읽기 모드로 열기
			data = json.load(f)
		result = ['None','None'] #단어가 사전에서 검색되지 않을 경우에 반환값, 초기값	
		for i in range(0, len(data)): 
			if data[i]['word'] == wordname: #i번째 단어와 사전을 비교해서 단어가 존재하는지 확인 존재하면 아래 코드 실행
				result.pop() #어근값과 극성치값 삭제
				result.pop()
				result.append(data[i]['word_root']) #데이터 리스트에 어근 추가
				result.append(data[i]['polarity'])	 #데이터 리스트에 극성치값 추가
		return int(result[1])

if __name__ == "__main__":
	
	ksl = KnuSL
	
	print("\nKNU 한국어 감성사전입니다~ :)")
	print("사전에 단어가 없는 경우 결과가 None으로 나타납니다!!!")
	print("종료하시려면 #을 입력해주세요!!!")
	print("-2:매우 부정, -1:부정, 0:중립 or Unkwon, 1:긍정, 2:매우 긍정")
	print("\n")	

	from konlpy.tag import Kkma #형태소 분석 라이브러리 임포트
	kkma = Kkma() #형태소 분석 라이브러리 객체화
	sent = []
	x = kkma.pos("음식이 맛도 없고 딱딱해서 짜증나고 끔찍했어요.") #형태소 분석 후 데이터 저장 데이터 형식은 리스트 안 딕셔너리

	score = 0
	for i in range(len(x)):
		if x[i][1] == "VA":
			sent.append(x[i][0]+"다") #VA(형용사) + 어미 '다' 로 사전 기본형 생성
		if x[i][1] == "VV":
			sent.append(x[i][0]+"다") #VV(동사) + 어미 '다' 로 사전 기본형 생성
		if x[i][1] == "MAG" and x[i + 1][1] == "VA":
			sent.append(x[i][0]+x[i + 1][0]+"다")
		"""y = ksl.sentiment_score(x[i][0] + "다")
		score += y[1] 	
		if i == len(x):
			score /= len(x)"""

	print(x) 
	for i in sent: print(i)

	for i in sent: 
		wordname = i
		wordname = wordname.strip(" ") #큰따옴표 제거		
		if wordname != "#": #사전 검색 유지
			print(ksl.data_list(wordname))
			print("\n")	
				

		elif wordname == "#": #사전 검색 종료
			print("\n이용해주셔서 감사합니다~ :)")
			break