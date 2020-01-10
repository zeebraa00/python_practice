# 파이썬 10일차

import openpyxl

wb=openpyxl.load_workbook("./파일입출력/수강신청.xlsx")
sheetname = wb.sheetnames
ws1=wb[sheetname[0]] # 첫 번째 시트
ws2=wb[sheetname[1]] # 두 번째 시트
ws3=wb[sheetname[2]] # 세 번째 시트

ws2data=list(map(list,ws2.values))
ws3data=list(map(list,ws3.values))

majorlist=[]
subjects ={}

for info in ws2data : # info는 row 당 배열로 받아와진다
  if info[0] not in majorlist :
    majorlist.append(info[0])
del(majorlist[0])

for info in ws3data : # info는 row 당 배열로 받아와진다
  subjects[info[0]]=info[1]
del(subjects['과목'])

while True :
  major=input("전공을 입력하세요 : ")
  if major in majorlist :
    break
  else :
    print("다시 입력하세요")
    print(majorlist)

while True :
  entry=[]
  lecture=input('과목을 입력하세요(종료=0) : ')
  if lecture =='0' :
    break
  if lecture not in subjects :
    print("존재하지 않는 과목입니다.")
    continue
  if subjects[lecture] == '폐강' :
    print("이번 학기에 폐강된 과목입니다.")
    continue
  
  entry.append(lecture)

  for info in ws2data :
    if (info[1] == lecture) :
      if info[2]=='교양' :
        entry.append('교양')
        print("교양 과목입니다.")
        break
      if (info[0]==major):
        entry.append(info[2])
        print(info[2],"(으)로 인정됩니다")
        break
      else :
        entry.append("교양")
        print("자신의 전공이 아니므로 교양으로 처리합니다")
        break
  print(entry)
  ws1.append(entry)

print('저장하고 종료합니다.')
wb.save('./파일입출력/수강신청.xlsx')