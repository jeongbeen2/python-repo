a = 1
b = 1

while b<=9:
    c = a*b
    print(a,"*",b,"=",f"{c}")
    b += 1
    if b == 10:
        a += 1
        b = 1
        if a == 10:
          break