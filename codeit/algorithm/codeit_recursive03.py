# n번째 피보나치 수를 리턴
def fib(n):
    # Recursive Case
    if n > 2:
        return fib(n - 1) + fib(n - 2)
    # Base Case
    return 1


# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))
