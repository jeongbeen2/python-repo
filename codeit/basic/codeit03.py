import os
os.system('cls')

first = 1
second = 1
i = 1

while i<=50:
    print(first)
    third = first + second
    first = second
    second = third
    i += 1
    