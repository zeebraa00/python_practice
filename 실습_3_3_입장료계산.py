# 파이썬 3일차

print(">>전망대 입장료 구하는 프로그램<<")

fast=input("Fast Pass를 원하십니까? (y/n)")
if (fast=="y") :
    print("입장료는 50000원입니다")

elif (fast=="n") :
    age=int(input("입장하는 인원의 연령을 만 나이로 입력하세요: "))
    if (12 < age) :
        print("입장료는 27000원입니다")
    elif (3<= age <=12 ):
        print("입장료는 24000원입니다")
    else :
        print("무료 입장 대상입니다")
else :
    print("input error")