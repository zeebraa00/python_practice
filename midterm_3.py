# 파이썬 8일차

list1=[] # 품명 저장
list2=[] # 가격 저장
price=0

def oper() :
  print("")
  print(">>제1공학관 자판기<<")
  print("1. 자판기 항목 추가")
  print("2. 구매 가능 품목 출력")
  print("3. 물품 구매")
  print("0. 종료")
  a=int(input("원하는 동작 : "))
  if (a == 1) :
    func1()
    oper()
  elif (a == 2) :
    func2()
    oper()
  elif (a == 3) :
    func3()
    oper()
  elif (a == 0) :
    print("자판기 프로그램 종료")
    exit()
  else :
    print("input error")
    oper()

def func1() :
  a=input("추가할 상품의 품명을 입력하세요(입력 완료=0) : ")
  if a=="0" :
    return
  elif a in list1 :
    print("이미 자판기에 있는 상품입니다.")
  else :
    b=int(input("상품의 가격을 100원의 배수로 입력하세요 : "))
    list1.append(a)
    list2.append(b)
  func1()

def func2() :
  if (len(list1)==0) :
    print("자판기에 아직 상품이 없습니다.")
  else :
    for i in range(len(list1)) :
      print(list1[i],":",list2[i])

def func3() :
  global price
  if (len(list1)==0) :
    print("자판기에 물건이 없어서 구매할 수 없습니다.")
  else :
    a=input("구매하실 상품을 입력하세요(선택 완료=0) : ")
    if (a=="0") :
      if (price == 0) :
        print("아무것도 선택하지 않았습니다.")
        oper()
      else :
        while True :
          money=int(input("입력하실 천원 권을 입력하세요."))
          if (price > money*1000) :
            print("액수가 부족합니다. 다시 입력하세요.")
          else :
            charge=money*1000-price
            c1=charge//500
            c2=(charge%500)/100
            print("500원 동전 %d개 반환"%c1)
            print("100원 동전 %d개 반환"%c2)
            oper()
    elif (a not in list1) :
      print("존재하지 않는 상품입니다.")
    else : 
      for i in range(len(list1)) :
        if (list1[i]==a) :
          price += list2[i]
    func3()

oper()