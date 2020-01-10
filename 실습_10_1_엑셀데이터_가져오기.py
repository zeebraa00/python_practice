# 파이썬 10일차

import openpyxl

wb=openpyxl.load_workbook('./파일입출력/서울지하철.xlsx')
ws=wb.active

# list(ws.values) 라고 저장하면 원소가 튜플로 저장됨
# 아래의 두 개는 같은 코드
subway=list(map(list, ws.values))
# subway=[]
# for line in ws.values :
#   line=list(line)
#   subway.append(line)

print(subway)