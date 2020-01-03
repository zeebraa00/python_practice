# 파이썬 5일차

def gugu() :
  num=int(input("원하는 단을 입력하세요(2-9단) : "))
  if (2<=num<=9) :
    for i in range(0,9,1) : 
      print("%d X %d = %d"%(num, i+1, num*(i+1)))
    gugu()
  elif (num==0) :
    exit()
  else :
    print("오류입니다.")
    gugu()
  
gugu()