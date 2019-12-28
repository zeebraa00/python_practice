# 파이썬 1일차

r=input("반지름을 입력하시오:")
r1=int(r)
r2=float(r)

area1=3*r1**2;len1=2*3*r1
area2=3.14*r2**2;len2=2*3.14*r2

print("명륜이가 구한 넓이: %d, 둘레: %d"%(area1, len1))
print("율전이가 구한 넓이: %.1f, 둘레: %.15f"%(area2, len2))
print("넓이오차: %.1f"%(area1-area2))
print("둘레오차: %.16f"%(len1-len2))

