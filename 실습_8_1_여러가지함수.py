# 수학과 2016314728 정재헌

# 실습1-1

def print_keyargs(**keyargs) :
  print(keyargs)

print_keyargs(value=10)
print_keyargs(name="강예서",age=18)

# 실습1-2

def introduce(name, adult=True) : # (adult=True, name) 안됨
  print("이름 : %s"%name)
  if adult :
    print("성인입니다.")
  else :
    print("성인이 아닙니다.")

introduce("김고은")
introduce("김고딩", False)

# 실습1-3

def add_some3(a,b) :
  return a+b, a*b
result = add_some3(3, 5)
print(result)
sum, mul= add_some3(3, 5)
print(sum, mul)

# 실습1-4

a = 1
def function3() :
  global a
  a += 1
function3()
print(a)

# 실습1-5

def flunk(x):
  return x < 60
score = [35, 67, 45, 21, 81]
for i in filter(flunk, score):
  print(i)

# 실습1-5와 같다
score = [35, 67, 45, 21, 81]
result = list( filter(lambda x: x<60, score) )
print(result)

# 실습1-6
def half(x):
  return x / 2
score = [35, 67, 45, 21, 81]
for i in map(half, score):
  print(i)

# 실습1-6과 같다
score = [35, 67, 45, 21, 81]
result= list( map(lambda x: x/2, score) )
print(result)