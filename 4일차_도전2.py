# 파이썬 4일차

import random

count=0

def oper() :
    global count
    count += 1

    while True :
        a=input("%d번째 시도 : 0~9 사이의 세 숫자를 공백을 사이에 두고 입력 : "%(count)).split()
        if (len(a)<3) :
            print("다시 입력하세요")
            oper()
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
            oper()
        else :
            if (cnt2==3) :
                print("WIN!")
                exit()
            else :
                print("%d 스트라이크, %d 볼"%(cnt2, cnt1-cnt2))
                oper()
            
list=[]

while True : # 중복없이 랜덤하게 3개의 번호 뽑기
    num = random.randrange(0,10) # 0 이상 10 미만의 정수
    if num in list :
        continue
    list.append(num)
    if len(list)==3 :
        break

print(">>숫자 야구 프로그램<<")

oper()