# 파이썬 2일차

lecture_credit = {
    "강의1":2,
    "강의2":1,
    "강의3":2,
    "강의4":3,
    "강의5":3,
    "강의6":3
    }
    
gpa = {
    "A+":4.5,"A":4.0,
    "B+":3.5,"B":3.0,
    "C+":2.5,"C":2.0
    }

my_grade= {
    "강의1":"A+",
    "강의2":"C",
    "강의3":"B+",
    "강의4":"A"
    }

total_credit=0
accum=0

for i in my_grade :
    print("강의명:",i)
    print("이수학점수",lecture_credit[i])
    print("개별gpa", gpa[my_grade[i]])
    total_credit += lecture_credit[i]
    accum += lecture_credit[i]*gpa[my_grade[i]]

print("성균이의 이번학기 학점은",accum/total_credit,"입니다")
