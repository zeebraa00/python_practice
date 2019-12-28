# 파이썬 2일차

print(">> 학생 정보 딕셔너리 <<");print("(학번 학과 이름 과제성적 을 띄어쓰기로 입력할 것)")

student={}

for i in range(0,5,1) :
    a=input("%d번째 학생의 정보를 입력하세요:"%(i+1)).split()
    student[a[0]]=a[1:]

# print("{}".format(student))

for i in student :
    print(i,student[i])
