# 파이썬 9일차

import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
inFile = open("./파일입출력/실습4.txt","r",encoding='UTF8')

data=inFile.readlines()
inFile.close()

ws.append(["","1월","2월","3월","4월","5월","6월","7월","8월","9월","10월","11월","12월"])

for i in range(len(data)) :
  a=data[i].split()
  ws.append(a)

wb.save("실습4.xlsx")