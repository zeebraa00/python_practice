# 파이썬 7일차

def oper() :
  a=input("수식(종료=q) : ").split()
  if(a[0]=="q") :
    return
  elif (len(a)==3):
    num1=int(a[0]);num2=int(a[2])
    if (a[1]=="+") :
      func1(num1,num2)
    elif (a[1]=="-") :
      func2(num1,num2)
    elif (a[1]=="*") :
      func3(num1,num2)
    elif (a[1]=="/") :
      func4(num1,num2)
    elif (a[1]=="**") :
      func5(num1,num2)
    elif (a[1]=="//") :
      func6(num1,num2)
    elif (a[1]=="%") :
      func7(num1,num2)
    else :
      print("input error")
      oper()
  else :
    print("input error")
    oper()

def func1(a,b) :
  print("연산의 결과 : %d"%(a+b))
  oper()

def func2(a,b) :
  print("연산의 결과 : %d"%(a-b))
  oper()

def func3(a,b) :
  print("연산의 결과 : %d"%(a*b))
  oper()

def func4(a,b) :
  print("연산의 결과 : %.2f"%(a/b))
  oper()

def func5(a,b) :
  print("연산의 결과 : %d"%(a**b))
  oper()

def func6(a,b) :
  print("연산의 결과 : %d"%(a//b))
  oper()

def func7(a,b) :
  print("연산의 결과 : %d"%(a%b))
  oper()
  
print(">>파이썬 연산자를 활용한 계산기<<")
print("계산하고자 하는 수식을 띄어 쓰기로 입력하세요 (ex) 3 ** 2\n")

oper()