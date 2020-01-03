# 파이썬 5일차

items=[1,2,3,4,5,6,7,8]

for i in range (0,8,1) :
  for j in range (i+1,8,1) :
    for k in range (j+1,8,1) :
      total = items[i]+items[j]+items[k]
      if total == 16 :
        print(items[i], items[j], items[k])
