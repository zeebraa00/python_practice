# 파이썬 7일차

def ck_semester() :
  a=int(input("총 등록 학기 수는? : "))
  if (a>=8) :
    print("등록 학기 횟수 기본 요건을 충족하였습니다.")
    return 1
  else :
    print("등록 학기 횟수 기본 요건을 충족하지 못하였습니다.")
    return 0

def ck_credit() :
  a=int(input("수강 완료한 학점 수는? : "))
  if (a>=130) :
    print("요구 학점을 만족하였습니다.")
    return 1
  else :
    print("요구 학점을 만족하지 못하였습니다.")
    return 0

def ck_gpa() :
  a=float(input("총평점 평균은? (4.5 만점) : "))
  if (a>=2.5) :
    print("졸업 기준 성적을 충족하였습니다.")
    return 1
  else :
    print("졸업 기준 성적을 충족하지 못하였습니다.")
    return 0

def ck_poom() :
  a=input("3품 취득여부 (y/n) : ")
  if (a == 'y') :
    print("3품 요건을 충족하였습니다.")
    return 1
  else :
    print("3품 요건을 충족하지 못하였습니다.")
    return 0

print("=====졸업요건 확인 프로그램입니다.=====")
if ck_semester() and ck_credit() and ck_gpa() and ck_poom()  :
  print("축하합니다. 모든 졸업 요건을 충족하셨습니다")
else :
  print("부족한 항목을 충족하셔서 졸업에 성공하시기 바랍니다.")