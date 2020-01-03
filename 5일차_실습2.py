# 파이썬 5일차

s=1

def oper() :
  global s
  print("현재위치 : %d층"%(s))

  while s < 12 :
    a=input("가위바위보 <이김> or <짐> 입력 : ")
    if (a=="이김") :
      s += 3
    elif (a=="짐") :
      if (s>1) :
        s -= 1
    else : 
      print("다시 입력해주세요")
      oper()

    print("현재위치 : %d층"%(s))
  print("게임 끝")

oper()