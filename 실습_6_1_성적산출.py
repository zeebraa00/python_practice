# 파이썬 6일차

list=[]

for i in range(0,5,1) :
  print("===%d번째 학생==="%(i+1))
  mid=int(input("중간고사 점수 입력 : "))
  final=int(input("기말고사 점수 입력 : "))
  list.append([mid,final])

for i in range (0,5,1) :
  if (list[i][0] < 20) or (list[i][1] < 20) :
    list[i].append("F")
  elif (170 < list[i][0]+list[i][1] <= 200) :
    list[i].append("A")
  elif (140 < list[i][0]+list[i][1] <= 170) :
    list[i].append("B")
  elif (110 < list[i][0]+list[i][1] <= 140) :
    list[i].append("C")
  else :
    list[i].append("D")

print("중간 기말 학점")
for i in range (0,5,1) :
  print("%3d %3d %3c"%(list[i][0],list[i][1],list[i][2]))