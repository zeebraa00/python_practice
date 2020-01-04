# 파이썬 6일차

# 실습3-1
n1=int(input("정수 입력 : "))
for i in range(0,n1,1) :
  print("*"*(n1-i))

# 실습3-2
n2=int(input("정수 입력 : "))
for i in range(0,n2,1) :
  print(" "*i+"*"*(n2-i))

# 실습3-3
n3=int(input("정수 입력 : "))
for i in range(0,n3,1) :
  print(" "*(i)+"*"*(2*n3-2*i-1)+" "*(i))

# 실습3-4
n4=int(input("정수 입력 : "))
for i in range(0,n4,1) :
  print("%d"%(i+1)*(i+1))
