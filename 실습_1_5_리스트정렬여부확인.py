# 파이썬 1일차

import copy

list=[]

for i in range (0,10,1):
    a=int(input("%d번째 자료를 입력하세요:"%(i+1)))
    list.append(a)

#print(list)

list1=copy.copy(list)

#print(list1)

for i in range (0,10,1):
    for j in range (i+1,10,1):
        if list[i] > list[j]:
            (list[i],list[j])=(list[j],list[i])

#print(list)
#print(list1)

if list==list1:
    print("오름차순으로 정렬된 자료입니다.")
else : 
    print("오름차순으로 정렬된 자료가 아닙니다.")
