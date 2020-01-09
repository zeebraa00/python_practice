# 파이썬 9일차

inFile = open("./파일입출력/실습1.txt","r")
outFile = open("./파일입출력/실습1_upper.txt","w")
for line in inFile : # 원본 파일에서 한 줄씩 읽어서
  outFile.write(line.upper()) # 대문자로 변환해서 새로운 파일에 쓰기
inFile.close()
outFile.close()
print("대문자로 파일이 변환되었습니다.")