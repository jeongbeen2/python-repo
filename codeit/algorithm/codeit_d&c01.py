def consecutive_sum(start, end):
    if start == end:
        return start

    mid = (start+end)//2
    left_sum = consecutive_sum(start, mid)
    right_sum = consecutive_sum(mid+1, end)
    return left_sum + right_sum

    # 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
