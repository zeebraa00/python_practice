# 파이썬 3일차

members={}

def oper() :
    a=input("로그인할 회원의 id를 입력하세요: ")
    b=input("로그인할 회원의 pw를 입력하세요: ")

    if a not in members :
        print("가입되지 않은 id입니다.")
        oper()
    else :
        if b == members[a] :
            print("%s계정으로 로그인 되었습니다"%(a))
        else :
            print("비밀번호 오류!")
            oper()

for i in range(0,3,1) :
    id=input("%d 번째 회원의 id를 입력하세요 : "%(i+1))
    pw=input("%d 번째 회원의 pw를 입력하세요 : "%(i+1))
    members[id]=pw

#print(members)

oper()
