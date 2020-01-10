# 파이썬 10일차

import openpyxl

wb = openpyxl.load_workbook('./파일입출력/서울지하철.xlsx')
ws=wb.active

subway=list(map(list, ws.values))
answer=[]

while True :
  line = input("지하철 노선을 입력하세요(1~4호선) : ")
  if line in ['1호선','2호선','3호선','4호선']:
    answer.extend(subway[int(line[0])-1])
    break
  else :
    print("다시 입력하세요(ex. 3호선)")

del(answer[0])
print(answer)

already=[]
while True :
  station=input(line+'의 정차역 입력(종료=0) : ')
  if station == '0' :
    print("지하철 게임 종료!")
    break
  else :
    if (station in answer) :
      if (station not in already) :
        already.append(station)
        print(already)
        print("존재하는 정차역입니다! 통과")
      else :
        print("이미 입력하신 역입니다! 벌칙")
    else :
      print("존재하지 않는 정차역입니다! 벌칙")