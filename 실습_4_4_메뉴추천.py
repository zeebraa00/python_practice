# 파이썬 4일차

def func1() :
  a1 = input("음식의 카테고리를 입력하세요[한식/중식/일식/양식] : ")
  global b1
  if (a1 == "한식") :
    b1 = 0
  elif (a1 == "중식") :
    b1 = 1
  elif (a1 == "일식") :
    b1 = 2
  elif (a1 == "양식") :
    b1 = 3
  else :
    print("다시 입력하세요")
    func1()

def func2() :
  a2 = input("국물 있는 음식을 선호하십니까? (네/아니오) : ")
  global b2
  if (a2 == "네") :
    b2 = 0
  elif (a2 == "아니오") :
    b2 = 1
  else :
    print("다시 입력하세요")
    func2()

def func3() :
  a3 = input("면 요리를 원하십니까? (네/아니오) : ")
  global b3
  if (a3 == "네") :
    b3 = 0
  elif (a3 == "아니오") :
    b3 = 1
  else :
    print("다시 입력하세요")
    func3()

def func4() :
  a4 = input("매운 음식을 원하십니까? (네/아니오) : ")
  global b4
  if (a4 == "네") :
    b4 = 0
  elif (a4 == "아니오") :
    b4 = 1
  else :
    print("다시 입력하세요")
    func4()

def oper() :
  for i in range (0,32,1) :
    if (food_list[i]["a1"]==b1 and food_list[i]["a2"]==b2 and food_list[i]["a3"]==b3 and food_list[i]["a4"]==b4) :
      print("<%s> 메뉴를 추천합니다"%(food_list[i]["menu"]))
      exit()

# food DB
food_list=[
  {"a1" : 0, "a2" : 0, "a3" : 0, "a4" : 0, "menu" : "음식1"}, 
  {"a1" : 0, "a2" : 0, "a3" : 0, "a4" : 1, "menu" : "음식2"}, 
  {"a1" : 0, "a2" : 0, "a3" : 1, "a4" : 0, "menu" : "음식3"}, 
  {"a1" : 0, "a2" : 0, "a3" : 1, "a4" : 1, "menu" : "음식4"}, 
  {"a1" : 0, "a2" : 1, "a3" : 0, "a4" : 0, "menu" : "음식5"}, 
  {"a1" : 0, "a2" : 1, "a3" : 0, "a4" : 1, "menu" : "음식6"},
  {"a1" : 0, "a2" : 1, "a3" : 1, "a4" : 0, "menu" : "음식7"}, 
  {"a1" : 0, "a2" : 1, "a3" : 1, "a4" : 1, "menu" : "음식8"}, 
  {"a1" : 1, "a2" : 0, "a3" : 0, "a4" : 0, "menu" : "음식9"}, 
  {"a1" : 1, "a2" : 0, "a3" : 0, "a4" : 1, "menu" : "음식10"},
  {"a1" : 1, "a2" : 0, "a3" : 1, "a4" : 0, "menu" : "음식11"}, 
  {"a1" : 1, "a2" : 0, "a3" : 1, "a4" : 1, "menu" : "음식12"}, 
  {"a1" : 1, "a2" : 1, "a3" : 0, "a4" : 0, "menu" : "음식13"}, 
  {"a1" : 1, "a2" : 1, "a3" : 0, "a4" : 1, "menu" : "음식14"}, 
  {"a1" : 1, "a2" : 1, "a3" : 1, "a4" : 0, "menu" : "음식15"},
  {"a1" : 1, "a2" : 1, "a3" : 1, "a4" : 1, "menu" : "음식16"}, 
  {"a1" : 2, "a2" : 0, "a3" : 0, "a4" : 0, "menu" : "음식17"}, 
  {"a1" : 2, "a2" : 0, "a3" : 0, "a4" : 1, "menu" : "음식18"}, 
  {"a1" : 2, "a2" : 0, "a3" : 1, "a4" : 0, "menu" : "음식19"},
  {"a1" : 2, "a2" : 0, "a3" : 1, "a4" : 1, "menu" : "음식20"}, 
  {"a1" : 2, "a2" : 1, "a3" : 0, "a4" : 0, "menu" : "음식21"}, 
  {"a1" : 2, "a2" : 1, "a3" : 0, "a4" : 1, "menu" : "음식22"}, 
  {"a1" : 2, "a2" : 1, "a3" : 1, "a4" : 0, "menu" : "음식23"}, 
  {"a1" : 2, "a2" : 1, "a3" : 1, "a4" : 1, "menu" : "음식24"}, 
  {"a1" : 3, "a2" : 0, "a3" : 0, "a4" : 0, "menu" : "음식25"},
  {"a1" : 3, "a2" : 0, "a3" : 0, "a4" : 1, "menu" : "음식26"}, 
  {"a1" : 3, "a2" : 0, "a3" : 1, "a4" : 0, "menu" : "음식27"}, 
  {"a1" : 3, "a2" : 0, "a3" : 1, "a4" : 1, "menu" : "음식28"},
  {"a1" : 3, "a2" : 1, "a3" : 0, "a4" : 0, "menu" : "음식29"}, 
  {"a1" : 3, "a2" : 1, "a3" : 0, "a4" : 1, "menu" : "음식30"}, 
  {"a1" : 3, "a2" : 1, "a3" : 1, "a4" : 0, "menu" : "음식31"}, 
  {"a1" : 3, "a2" : 1, "a3" : 1, "a4" : 1, "menu" : "음식32"}
]

func1();func2();func3();func4()
oper()