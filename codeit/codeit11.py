numbers = [2, 3, 5, 7, 11, 13, 17, 19]
new = []
# 리스트 뒤집기
# 코드를 입력하세요.
i = 1
for num in numbers:
    new.append(numbers[-i])
    i += 1

    
print("뒤집어진 리스트: " + str(new))

print("test!")