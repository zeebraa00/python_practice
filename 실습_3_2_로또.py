# 파이썬 3일차

import random

lotto=[]

while True : # 중복없이 랜덤하게 6개의 번호 뽑기
    num = random.randrange(1, 26) # 1 이상 26 미만의 정수
    if num in lotto :
        continue
    lotto.append(num)
    if len(lotto)==6 :
        break

print(lotto)
print("")
print(">>6/25 로또<<")
a=input("1부터 25까지 6개의 숫자를 입력하세요:").split()

count=0

for i in range(0,6,1) :
    if int(a[i]) in lotto :
        print("%d 매치!"%(int(a[i])))
        count +=1
    else :
        print("%d 없음!"%(int(a[i])))

if count!=6 :
    print("총 6개 숫자 중 %d개를 맞추셨습니다. 다음 기회에..."%(count))
elif count==6 :
    print("로또 당첨! 당첨금을 수령하세요")
else :
    print("error")
