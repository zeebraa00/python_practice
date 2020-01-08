# 수학과 2016314728 정재헌

numbers = [5, 21, 34, 6, 10, 26, 89, 8, 43]

def func1(a) :
  a.sort()
  leng=len(numbers)
  print("1. 최소값 : ",a[0]," 최대값 : ",a[leng-1])

def func2(a) :
  even=0;odd=0
  for i in range (0,len(numbers),1) :
    if (numbers[i] % 2 == 0) :
      even += numbers[i]
    else :
      odd += numbers[i]
  print("2. 홀수합 : ",odd," 짝수합 : ",even)

def func3(a) :
  mult=1
  for i in range(len(numbers)) :
    mult *= numbers[i]
  print("3. 모든 자료의 곱 : ",mult)

def func4(a) :
  sum=0
  for i in range(len(numbers)) :
    sum += numbers[i]
  average = sum/len(numbers)
  print("4. 산술 평균 : ",average)

func1(numbers)
func2(numbers)
func3(numbers)
func4(numbers)