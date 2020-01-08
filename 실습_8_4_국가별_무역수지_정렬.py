# 수학과 2016314728 정재헌

db = []

def enter() :
  a=input("국가명(종료:0) : ")
  if a=="0" :
    return
  else :
    b=int(input("수입 : "))
    c=int(input("수출 : "))
    db.append([a,[b,c,c-b]])
    enter()

def func1() :
  db.sort(key=lambda x:x[0])
  # print(db)
  print("%s %s %s"%("국가명","수입액","수출액"))
  print("-----------------------")
  for i in range(len(db)) :
    print("%s %7d %7d"%(db[i][0],db[i][1][0],db[i][1][1]))
  print("")

def func2() :
  db.sort(key=lambda x:x[1][2], reverse=True)
  # print(db)
  print("%s %s"%("국가명", "순이익"))
  print("-----------------------")
  for i in range(len(db)) :
    print("%s %7d"%(db[i][0],db[i][1][2]))
  print("")

def oper() :
  a=int(input("1:국가순 정렬, 2:순이익순 정렬, 이외 : 종료 "))
  if a==1 :
    func1()
    oper()
  elif a==2 :
    func2()
    oper()
  else :
    return

enter()
oper()