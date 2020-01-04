# 파이썬 중간고사 대체과제2

date=[] # 가능한 날짜 저장

ck=[0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0] # 각 날짜별로 몇 명이 가능한지 체크

ok=[] # 모두 만날 수 있는 날짜 저장

num=0 # 사람 수 체크

def date_input() :
  global num
  buffer=[] # 중복체크 방지용 버퍼
  a=input("가능한 날짜 : ").split()
  num+=1
  if (a[0]=="q") :
    num-=1
    return
  for i in range(0,len(a),1) :
    if (len(a[i]) <= 2) :
      if int(a[i]) in buffer : # 중복 여부 체크
        continue
      else :
        buffer.append(int(a[i]))
    else :
      buff=[]
      buff.extend(a[i].split("~"))
      first=int(buff[0])
      last=int(buff[1])
      term=last-first
      if (term != 1) :
        buff=[]
        for i in range(0,term+1,1) :
          buff.append(first+i)
      # date.extend(buff) # 이렇게 하면 중복체크 고려 못함
      for i in range(0,len(buff),1) : # 중복 여부 체크
        if (buff[i] in buffer) :
          continue
        else :
          buffer.append(buff[i])
  date.extend(buffer)
  date_input()

date_input()

for i in range(0,len(date),1) : # ck 리스트 채우기
  ck[int(date[i])-1] +=1

for i in range(0,31,1) : # ok 리스트 채우기
  if (ck[i]>=num) :
    ok.append(i+1)

print("<%d명이 모두 가능한 날>"%(num))
if (len(ok)==0) :
  print("없습니다. 다음 기회에...")
else : 
  for i in range (0,len(ok),1) :
    print("%d일"%(ok[i]), end=" ")