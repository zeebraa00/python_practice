# 수학과 2016314728 정재헌

def oper() :
  region = str(input("여행하려는 국가를 입력하세요 : "))
  remain_month = int(input("지금으로부터 몇 개월 이후에 여행할 계획입니까? : "))
  
  if (region not in asia) and (region not in europe) and (region not in us) :
    print("해당 지역에는 취항 노선이 없습니다.")
    print("===============restart===============")
    oper()
  else :
    if (region in asia):
      if (remain_month < 3) :
        print("얼리버드 항공권 예약 대상이 아닙니다.")
        print("===============restart===============")
        oper()
      elif (3 <= remain_month < 6) :
        print("%s지역, 잔여기간 3개월 이상 6개월 미만인 경우 할인율은 6%%입니다."%(region))
        print("===============restart===============")
        oper()
      elif (6 <= remain_month < 12) :
        print("%s지역, 잔여기간 6개월 이상 12개월 미만인 경우 할인율은 15%%입니다."%(region))
        print("===============restart===============")
        oper()
      elif (12 <= remain_month) :
        print("%s지역, 잔여기간 12개월 이상인 경우 할인율은 25%%입니다."%(region))
        print("===============restart===============")
        oper()
      else :
        print("error")
    elif (region in europe) :
      if (remain_month < 3) :
        print("얼리버드 항공권 예약 대상이 아닙니다.")
        print("===============restart===============")
        oper()
      elif (3 <= remain_month < 6) :
        print("%s지역, 잔여기간 3개월 이상 6개월 미만인 경우 할인율은 9%%입니다."%(region))
        print("===============restart===============")
        oper()
      elif (6 <= remain_month < 12) :
        print("%s지역, 잔여기간 6개월 이상 12개월 미만인 경우 할인율은 17%%입니다."%(region))
        print("===============restart===============")
        oper()
      elif (12 <= remain_month) :
        print("%s지역, 잔여기간 12개월 이상인 경우 할인율은 30%%입니다."%(region))
        print("===============restart===============")
        oper()
      else :
        print("error")
    else :
      if (remain_month < 3) :
        print("얼리버드 항공권 예약 대상이 아닙니다.")
        print("===============restart===============")
        oper()
      elif (3 <= remain_month < 6) :
        print("%s지역, 잔여기간 3개월 이상 6개월 미만인 경우 할인율은 10%%입니다."%(region))
        print("===============restart===============")
        oper()
      elif (6 <= remain_month < 12) :
        print("%s지역, 잔여기간 6개월 이상 12개월 미만인 경우 할인율은 20%%입니다."%(region))
        print("===============restart===============")
        oper()
      elif (12 <= remain_month) :
        print("%s지역, 잔여기간 12개월 이상인 경우 할인율은 40%%입니다."%(region))
        print("===============restart===============")
        oper()
      else :
        print("error")

asia = ["중국","일본","싱가포르"]
europe = ["영국", "프랑스", "독일"]
us = ["뉴욕", "워싱턴", "시카고"]

oper()