# 수학과 2016314728 정재헌

year=int(input("연도 입력 : "))
month=int(input("월 입력 : "))

m30=[4,6,9,11]
m31=[1,3,5,7,8,10,12]

if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)) : # 윤년 체크
  print("해당 년도는 윤년이므로 1년이 총 366일입니다.")
  if (month in m30) :
    print("%d년 %d월은 %d일까지 있습니다."%(year, month, 30))
  elif (month in m31) :
    print("%d년 %d월은 %d일까지 있습니다."%(year, month, 31))
  elif (month == 2) :
    print("%d년 %d월은 %d일까지 있습니다."%(year, month, 29))
  else : 
    print("input error (1부터 12 사이의 정수를 입력하세요)")
else : 
  print("해당 년도는 1년이 365일입니다.")
  if (month in m30) :
    print("%d년 %d월은 %d일까지 있습니다."%(year, month, 30))
  elif (month in m31) :
    print("%d년 %d월은 %d일까지 있습니다."%(year, month, 31))
  elif (month == 2) :
    print("%d년 %d월은 %d일까지 있습니다."%(year, month, 28))
  else : 
    print("input error (1부터 12 사이의 정수를 입력하세요)")
