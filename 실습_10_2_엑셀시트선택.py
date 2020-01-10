# 파이썬 10일차

import openpyxl

wb=openpyxl.load_workbook("./파일입출력/수강신청.xlsx")
sheetname = wb.sheetnames

ws1=wb[sheetname[0]] # 첫 번째 시트
ws2=wb[sheetname[1]] # 두 번째 시트
ws3=wb[sheetname[2]] # 세 번째 시트
ws3=wb["개설과목"] # 시트의 이름을 알고 있는 경우