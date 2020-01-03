# 파이썬 5일차

print("분야 : 철학/사회과학/자연과학/예술/역사")

list1=[] # 제목 저장
list2=[] # 분야 저장
list3=[] # 번호 저장

def oper() :
  print("===책제목과 분야를 입력해주세요(종료 : Q)===")
  a=input("첵제목 : ")
  if (a=="Q") :
    return
  b=input("분야 : ")
  if (b=="철학") :
    c=100
  elif (b=="사회과학") :
    c=200
  elif (b=="자연과학") :
    c=300
  elif (b=="예술") :
    c=400
  elif (b=="역사") :
    c=500
  else :
    c=900

  list1.append(a)
  list2.append(c)
  list3.append(b)
  oper()

oper()

for i in range (0,len(list1),1) :
  for j in range (i+1,len(list1),1) :
    if (int(list2[i]) > int(list2[j])) :
      (list1[i],list1[j])=(list1[j],list1[i])
      (list2[i],list2[j])=(list2[j],list2[i])
      (list3[i],list3[j])=(list3[j],list3[i])

print("====도서관 책 정렬목록====")
print("<제목> <분야>")
for i in range (0,len(list1),1) :
  print("%3s %3s"%(list1[i],list3[i]))