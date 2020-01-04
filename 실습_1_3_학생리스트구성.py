# 파이썬 1일차

print("학생 다섯 명의 정보를 입력하세요");print("(학과 학번 이름 과제성적 을 띄어 쓰기로 입력할 것)")

p=[]

for i in range(0,5,1):
    a=input("%d 번째 학생의 정보를 입력하세요:"%(i+1)).split()
    p.append(a)

print("{}".format(p))
