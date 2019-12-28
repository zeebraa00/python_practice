# 파이썬 2일차

dict={
    "명성대학":[100, 200, 300, 400],
    "스타대학":[10,20,40,80],
    "블루문대학":[3,5,90,70]
    }

print("=====분기별 대학 기부금 목록=====")

print("{}".format(dict))

a=input("대학이름:")
ave=(dict[a][0]+dict[a][1]+dict[a][2]+dict[a][3])/4
print("%s의 분기별 기부금의 평균은 %d억원입니다."%(a,ave))

print("")
print("=====분기별 대학 기부금 목록=====")

print("{}".format(dict))
      
b=input("대학이름:")
c=int(input("몇 분기의 기부금?"))

print("%s의 %d분기 기부금은 %d억원입니다."%(b,c,dict[b][c-1]))
