import os
os.system('cls')

num = 120
div = 1
count = 0

while div<=120:
  if num % div == 0:
    print(div)
    count += 1
  div += 1

print(f"{num}의 약수는 총 {count}개 입니다.")

