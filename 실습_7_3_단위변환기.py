# 파이썬 7일차

def oper() :
  a=int(input("단위변환 : 1.길이 2.넓이 3.무게 4.부피 5.온도 6.종료 :"))
  if a==1 :
    b=int(input("길이단위 : 1.cm → inch 2.inch → cm : "))
    c=float(input("길이를 입력하세요 : "))
    print("입력한 %.2f을 변환하면 %.2f 입니다."%(c,length(b,c)));print()
    oper()
  elif a==2 :
    b=int(input("넓이단위 : 1.제곱미터 → 평 2.평 → 제곱미터 : "))
    c=int(input("넓이를 입력하세요 : "))
    print("입력한 %.2f을 변환하면 %.2f 입니다."%(c,area(b,c)));print()
    oper()
  elif a==3 :
    b=int(input("무게단위 : 1.그램 → 온스 2.온스 → 그램 : "))
    c=int(input("무게를 입력하세요 : "))
    print("입력한 %.2f을 변환하면 %.2f 입니다."%(c,weight(b,c)));print()
    oper()
  elif a==4 :
    b=int(input("부피단위 : 1.리터 → 갤런 2.갤런 → 리터 : "))
    c=int(input("부피를 입력하세요 : "))
    print("입력한 %.2f을 변환하면 %.2f 입니다."%(c,volume(b,c)));print()
    oper()
  elif a==5 :
    b=int(input("온도단위 : 1.섭씨 → 화씨 2.화씨 → 섭씨"))
    c=int(input("온도를 입력하세요 : "))
    print("입력한 %.2f을 변환하면 %.2f 입니다."%(c,temperature(b,c)));print()
    oper()
  elif a==6 :
    print("종료")
    return
  else :
    print("error");print()
    oper()

def length(change_type, value):
  if change_type== 1:
    result = value / 2.54
  elif change_type== 2:
    result = value * 2.54
  return result

def area(change_type, value):
  # 1제곱미터⇒0.3025 평, 1평⇒3.3058제곱미터
  if change_type== 1:
    result = value * 0.3025
  elif change_type== 2:
    result = value * 3.3058
  return result

def weight(change_type, value):
  # 1그램⇒0.035온스, 1온스⇒28.35그램
  if change_type== 1:
    result = value * 0.035
  elif change_type== 2:
    result = value * 28.35
  return result

def volume(change_type, value):
  # 1리터⇒0.26 갤런, 1갤런⇒3.79리터
  if change_type== 1:
    result = value * 0.26
  elif change_type== 2:
    result = value * 3.79
  return result

def temperature(change_type, value):
  # 1섭씨⇒섭씨*1.8+32 화씨, 1화씨⇒(화씨-32)/1.8 섭씨
  if change_type== 1:
    result = value*1.82+32
  elif change_type== 2:
    result = (value-32)/1.8
  return result

oper()