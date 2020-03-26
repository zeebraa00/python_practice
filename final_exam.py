# 파이썬 기말고사 (코딩시험)

import openpyxl

wb=openpyxl.load_workbook('./파일입출력/course.xlsx')
sheetname = wb.sheetnames
ws1=wb[sheetname[0]]
ws2=wb[sheetname[1]]
ws3=wb[sheetname[2]]

# 데이터 전처리
ws1data=list(map(list,ws1.values))
del(ws1data[0])
list1=[]
for info in ws1data :
  list1.append(info)
  
ws2data=list(map(list,ws2.values))
del(ws2data[0])
list2=[]
for info in ws2data :
  list2.append(info)

ws3data=list(map(list,ws3.values))
del(ws3data[0])
list3=[]
for info in ws3data :
    list3.append(info)

student_numbers=[]
for i in range(len(list3)) :
    student_numbers.append(list3[i][0])

subject_list=[]
for i in range(len(list2)) :
    subject_list.append(list2[i][1])

def func1() : # 수강 강좌 입력
    b=1
    while True :
        b=input("학번(0:종료) : ")
        if b=="0" :
            break
        if (b not in student_numbers) :
            print("존재하지 않는 학번입니다.")
            continue
        print("");print(" < 수강 강좌 입력 >");print("")
        semester=input("수강학기 : ")
        subject=input("과목명 : ")
        if (subject not in subject_list) :
            print("존재하지 않는 과목명입니다.")
            continue
        grade=input("취득학점(A,B,C,F) : ")
        if (grade not in ["A","B","C","F"]) :
            print("학점 잘못 입력")
            continue
        for i in range(len(list2)) :
            if subject == list2[i][1] :
                number=list2[i][0]
                break
        buff=[len(ws1['A']),b,semester,number,subject,grade]
        ws1.append(buff)
        #wb.save('course.xlsx')


def func2() : # 수강 강좌 확인
    
    # list1 최신화
    ws1data=list(map(list,ws1.values))
    del(ws1data[0])
    list1=[]
    for info in ws1data :
      list1.append(info)
      
    output=[]
    b=1
    while True :
        b=input("학번(0:종료) : ")
        if b=="0" :
            break
        if (b not in student_numbers) :
            print("존재하지 않는 학번입니다.")
            continue
        for i in range(len(list1)) :
            if b==list1[i][1] :
                output.append(list1[i])
        print("%10s %10s"%("과목명","학점"))
        print("-"*30)
        for i in range(len(output)) :
            print("%10s %10s"%(output[i][4],output[i][5]))
        print("-"*30)
        

while True :
    a=input("1.수강 강좌 입력 2.수강 강좌 확인 0.종료 : ")
    if a=="1" :
        func1()
    elif a=="2" :
        func2()
    elif a=="0" :
        print("< 초간단 수강 강좌 관리 시스템 종료! >")
        break
    else :
        print("없는 메뉴")

wb.save('./파일입출력/course.xlsx')
