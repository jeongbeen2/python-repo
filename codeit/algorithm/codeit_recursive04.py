# 1부터 n까지의 합을 리턴
def triangle_number(n):
    # Recursive Case
    if n >= 2:
        return n + triangle_number(n - 1)

    # Base Case
    return 1


# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))
