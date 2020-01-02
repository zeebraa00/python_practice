# 파이썬 4일차

list=[]

for i in range (0,3,1) :
  a=int(input("변의 길이를 입력하세요 : "))
  list.append(a)

for i in range (0,3,1):
  for j in range (i+1,3,1):
    if list[i] > list[j]:
      (list[i],list[j])=(list[j],list[i])

b=0;c=0

if (list[2] < list[0] + list[1]) :
  b=1 # 삼각형 맞다
  if (list[2]**2 < list[0]**2 + list[1]**2) :
    c=1 # 예각
  elif (list[2]**2 == list[0]**2 + list[1]**2) :
    c=2 # 직각
  else :
    c=3 # 둔각

if (b==0) :
  print("삼각형이 아닙니다")
elif (b==1) :
  if (c==1) :
    print("예각 삼각형입니다")
  elif (c==2) :
    print("직각 삼각형입니다")
  else :
    print("둔각 삼각형입니다")