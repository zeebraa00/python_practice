# 파이썬 6일차

import random
import time

n=0 # 맞은 개수

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

word = ["동해물과", "백두산이", "마르고", "닳도록",
        "하느님이", "보우하사", "우리나라", "만세",
        "무궁화", "삼천리", "화려", "강산", "대한",
        "사람", "대한으로", "길이", "보전하세"]

input("타자게임을 시작하려면 엔터를 눌러주세요.")

start = time.time()
oper()
end = time.time()

print("타자 시간 : %2f초"%(end - start))
print("맞은 단어 : %d"%(n))