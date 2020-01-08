# 파이썬 8일차

def factorial(n) :
  if n==1 :
    return 1
  return n*factorial(n-1)

def fibonacci(n) :
  if n==1 or n==2:
    return 1
  return fibonacci(n-1)+fibonacci(n-2)

def depth(n,i=0) :
  if i<n :
    i+=1
    print(i,"번째 깊이입니다")
    depth(n,i)

print(factorial(7))
print(fibonacci(6))
depth(6)