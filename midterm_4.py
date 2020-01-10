# 파이썬 10일차

import openpyxl

wb=openpyxl.load_workbook("./파일입출력/전국자전거길.xlsx")
sheetname = wb.sheetnames
ws1=wb[sheetname[0]]
ws2=wb[sheetname[1]]

# 데이터 전처리
ws1data=list(map(list,ws1.values))
del(ws1data[0])
adress=[]
for info in ws1data :
  adress.append(info[2])
  
ws2data=list(map(list,ws2.values))
del(ws2data[0])
interval=[]
for info in ws2data :
  interval.append(info[0])

def func1() :
  print("")
  print("[자전거길 국토종주 추천 구간]")
  for i in range(len(interval)) :
    print("%d. %s"%(i+1,interval[i]))
  print("")

def func2() :
  print("")
  print("[자전거길 국토종주 구간 정보]")
  while True :
    a=input("구간을 입력하세요 : ")
    if a not in interval :
      print("존재하지 않는 구간입니다. 다시 입력하세요!")
      continue
    else :
      break
  for i in range(len(ws2data)) :
    if (ws2data[i][0]==a) :
      print("거리 : %s"%(ws2data[i][1]))
      print("시간 : %s"%(ws2data[i][2]))
      print("난이도 :",int(ws2data[i][3])*"★")
      print("코스 정보 : %s"%(ws2data[i][4]))
  print("")

def func3() :
  print("")
  print("[자전거길 국토종주 지역별 인증센터]")
  while True :
    output=[]
    a=input("지역을 입력하세요. (ex. 서울, 부산, 강원) : ")
    for i in range(len(adress)) :
      if (adress[i].find(a) != -1) :
        output.append(ws1data[i])
    if (len(output)==0) : 
      print("해당 지역에 센터가 없습니다. 다시 입력하세요.")
      continue
    for i in range(len(output)) :
      print("[%s], %s"%(output[i][1],output[i][2]))
    break
  print("")

while True :
  print(">>국토종주 자전거길<<")
  print("1. 추천 구간")
  print("2. 구간 정보")
  print("3. 지역별 인증센터")
  print("0. 종료")
  a=input("원하는 동작 : ")
  if a=="1" :
    func1()
  elif a=="2" :
    func2()
  elif a=="3" :
    func3()
  elif a=="0" :
    print("프로그램을 종료합니다.")
    break
  else :
    print("다시 입력하세요!");print("")