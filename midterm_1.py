# 파이썬 중간고사 대체과제1

dict={}

def func0(): # 종료
    print("종료합니다")
    exit()

def func1(): # 추가
    word=str(input("영단어 입력:"))
    mean=str(input("뜻 입력:"))
    if word in dict :
        print("사전에 이미 있는 단어입니다. 뜻을 변경합니다.")
        dict[word]=mean
    else :
        dict[word] = mean

def func2(): # 삭제
    word=str(input("영단어 입력:"))
    if word in dict :
        del dict[word]
    else :
        print("사전에 없는 단어입니다.")
        
def func3(): # 검색
    word=str(input("영단어 입력:"))
    if word in dict :
        print("%s 의 뜻은 %s 입니다"%(word,dict[word]))
    else :
        print("사전에 없는 단어입니다.")

def func4(): # 사전 출력
    print(dict)

def oper() :
    print("*"*15)
    a=int(input("0.종료\n1.추가\n2.삭제\n3.검색\n4.사전 출력\n"))
    if a==0 :
        func0()
    elif a==1 :
        func1()
        oper()
    elif a==2 :
        func2()
        oper()
    elif a==3 :
        func3()
        oper()
    elif a==4 :
        func4()
        oper()
    else :
        print("다시 입력하세요")
        oper()
    
oper()