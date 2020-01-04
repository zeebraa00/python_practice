# 파이썬 6일차

num=int(input("단 입력 : "))

for i in range (num,0,-1) :
  print("===%d단==="%(i))
  for j in range (9,0,-1) :
    print("%d * %d = %d"%(i,j,i*j))