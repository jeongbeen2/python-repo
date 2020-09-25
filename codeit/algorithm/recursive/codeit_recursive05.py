# n의 각 자릿수의 합을 리턴
def sum_digits(n):

    # Recursive Case
    if n > 10:
        m = n - ((n // 10) * 10)  # n%10 = m
        return m + sum_digits(n // 10)

    # Base Case
    return n


# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
