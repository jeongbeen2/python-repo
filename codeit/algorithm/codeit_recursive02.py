n = int(input())


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(n))

# for 문


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(5))