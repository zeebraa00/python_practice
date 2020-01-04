# 파이썬 3일차

# 현재 시간 10:30, 약속 시간 17:00

t1=int(input("과제 1의 소요 시간을 분(min) 단위로 입력 :"))
t2=int(input("과제 2의 소요 시간을 분(min) 단위로 입력 :"))
t3=int(input("과제 3의 소요 시간을 분(min) 단위로 입력 :"))

if (t1<0) or (t2<0) or (t3<0) :
    print("input error")
    exit()

t=t1+t2+t3

min = (30 + t%60)%60
buff = (30 + t%60)//60 # 60진법 올림
hour = (10 + t//60 + buff)%12
noon = (10 + t//60 + buff)//12 # 0이면 오전 1이면 오후

if (noon==0) :
    print("오전 %d시 %d분에 과제를 마쳤으니 세리를 만날 수 있다!"%(hour, min))
elif (noon==1) :
    if (hour >= 5) :
        if (min > 0) :
            print("오후 %d시 %d분에 과제를 마치게 되어 세리를 만날 수 없다!"%(hour, min))
        else :
            print("오후 %d시 %d분에 과제를 마치게 되었으니 세리를 만날 수 있다!" %(hour, min))
    else :
        if (hour == 0):
            our = 12
        print("오후 %d시 %d분에 과제를 마치게 되었으니 세리를 만날 수 있다!" %(hour, min))
else :
    print("이미 하루가 지나서 세리를 만날 수 없다!")