# 파이썬 7일차

def oper() :
  a=input("생년월일 입력(yyyy/mm/dd) : ").split("/")
  age(a)
  star(a)

def age(a) :
  print("올해 2020년에는 %d살 입니다."%(2020-int(a[0])+1))

def star(a) :
  birthday=a[1]+a[2]
  birthday=int(birthday)
  if (321<=birthday<420) :
    print("당신의 별자리는 %s 입니다."%("양자리"))
  elif (420<=birthday<521) :
    print("당신의 별자리는 %s 입니다."%("황소자리"))
  elif (521<=birthday<622) :
    print("당신의 별자리는 %s 입니다."%("쌍둥이자리"))
  elif (622<=birthday<723) :
    print("당신의 별자리는 %s 입니다."%("게자리"))
  elif (723<=birthday<823) :
    print("당신의 별자리는 %s 입니다."%("사자자리"))
  elif (823<=birthday<923) :
    print("당신의 별자리는 %s 입니다."%("처녀자리"))
  elif (923<=birthday<1023) :
    print("당신의 별자리는 %s 입니다."%("천칭자리"))
  elif (1023<=birthday<1123) :
    print("당신의 별자리는 %s 입니다."%("전갈자리"))
  elif (1123<=birthday<1222) :
    print("당신의 별자리는 %s 입니다."%("사수자리"))
  elif (1222<=birthday) or (birthday<120) :
    print("당신의 별자리는 %s 입니다."%("염소자리"))
  elif (120<=birthday<219) :
    print("당신의 별자리는 %s 입니다."%("물병자리"))
  elif (219<=birthday<321) :
    print("당신의 별자리는 %s 입니다."%("물고기자리"))
  else :
    print("error")

print(">>나이와 별자리 알아보기<<")
oper()