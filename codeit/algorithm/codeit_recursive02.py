n = int(input())


def factorial(n):
    # Base Case
    if n <= 1:
        return 1
    # Recursive Case
    return n * factorial(n - 1)


print(factorial(n))
