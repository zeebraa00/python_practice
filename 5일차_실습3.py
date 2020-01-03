# 파이썬 5일차

def oper() :
  a = int(input("끝 숫자 입력 : "))
  print("1의 자리가 3의 배수인 경우에는 짝을 입력해주세요. 1부터 게임 시작!")

  for i in range (0,a,1) :
    ans=input("입력해주세요 : ")
    if (((i+1) % 10) == 3) or (((i+1) % 10) == 6) or (((i+1) % 10) == 9) : # 박수 칠 차례
      if (ans == "짝") :
        continue
      else :
        print("==틀렸습니다==")
        oper()
    else : # 박수 치면 안됨
      if (ans != str(i+1)) :
        print("==틀렸습니다==")
        oper()
      else :
        continue

oper()