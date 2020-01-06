# 파이썬 7일차

import random
import time

n=0
count=0
list=[]
word = ["동해물과", "백두산이", "마르고", "닳도록",
        "하느님이", "보우하사", "우리나라", "만세",
        "무궁화", "삼천리", "화려", "강산", "대한",
        "사람", "대한으로", "길이", "보전하세"]

def game1() : # 가위바위보
  wsp=['가위','바위','보']
  w=random.choice(wsp)
  a=input("가위, 바위, 보 중에서 하나를 입력하세요 : ")
  if (a not in wsp) :
    print("input error")
  if (w==a) :
    print("비겼습니다.")
    print("가위바위보 종료\n")
  else :
    if w=='가위' :
      if a=='바위' :
        print("이겼습니다.")
        print("가위바위보 종료\n")
      else :
        print("졌습니다.")
        print("가위바위보 종료\n")
    elif w=='바위' :
      if a=='보' :
        print("이겼습니다.")
        print("가위바위보 종료\n")
      else :
        print("졌습니다.")
        print("가위바위보 종료\n")
    elif w=='보' :
      if a=='가위' :
        print("이겼습니다.")
        print("가위바위보 종료\n")
      else :
        print("졌습니다.")
        print("가위바위보 종료\n")
    
def game2() : # 숫자맞추기
  a = random.randrange(1,21) # 1 이상 21 미만의 정수
  print(">>컴퓨터가 생각한 1~20 숫자 맞추기<<")
  while True :
    b=int(input("숫자를 입력하세요 (종료0)"))
    if (b==0) :
      print("종료")
      break
    else :
      if (b>a) :
        print("더 작은 숫자를 입력하세요")
      elif (a>b) :
        print("더 큰 숫자를 입력하세요")
      else :
        print("정답입니다.")
        print("숫자맞추기 게임 종료\n")
        break

def game3() : # 타자게임
  input("타자게임을 시작하려면 엔터를 눌러주세요.")

  start = time.time()
  oper()
  end = time.time()

  print("타자 시간 : %2f초"%(end - start))
  print("맞은 단어 : %d"%(n))
  print("타자게임 종료\n")

def game4() : # 숫자야구
  global list
  
  while True : # 중복없이 랜덤하게 3개의 번호 뽑기
      num = random.randrange(0,10) # 0 이상 10 미만의 정수
      if num in list :
          continue
      list.append(num)
      if len(list)==3 :
          break
  print(">>숫자 야구 프로그램<<")
  oper1()
  print("숫자야구 게임 종료\n")

def launcher() :
  print(">>성균이의 미니게임 런쳐<<")
  print("1. 가위바위보 2. 숫자맞추기 3. 타자연습 4. 숫자야구 0. 종료")
  a=int(input("실행을 원하는 게임"))
  if (a==1) :
    game1()
    launcher()
  elif (a==2) :
    game2()
    launcher()
  elif (a==3) :
    game3()
    launcher()
  elif (a==4) :
    game4()
    launcher()
  elif (a==0) :
    print("게임 런쳐를 종료합니다...")
    return
  else :
    print("error")
    launcher()

def oper() :
  global n
  i=0
  w=random.choice(word) # 리스트에서 랜덤으로 한 요소를 추출
  while True :
    a=input("문제 %d (종료는 !입력):%s\n"%(i+1,w));i+=1
    if a=="!" :
      return
    elif a==w :
      print("맞음!")
      n+=1
      w=random.choice(word) # 새로운 단어 추출
      continue
    else :
      print("틀림! 다시!")
      continue

def oper1() :
    global count
    count += 1

    while True :
        a=input("%d번째 시도 : 0~9 사이의 세 숫자를 공백을 사이에 두고 입력 : "%(count)).split()
        if (len(a)<3) :
            print("다시 입력하세요")
            oper1()
        for i in range (0,3,1) :
            a[i]=int(a[i])    

        cnt1=0;cnt2=0

        for i in range (0,3,1) :
            if a[i] in list :
                cnt1 += 1 # strike, ball 합친 개수
        for i in range (0,3,1) :
            if a[i] == list[i] :
                cnt2 += 1 # strike 개수
        
        if (cnt1==0) :
            print("out")
            oper1()
        else :
            if (cnt2==3) :
                print("WIN!")
                exit()
            else :
                print("%d 스트라이크, %d 볼"%(cnt2, cnt1-cnt2))
                oper1()

launcher()