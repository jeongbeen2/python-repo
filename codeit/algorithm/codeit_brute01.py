def max_product(left_cards, right_cards):

    # result값을 1로 설정.
    result = 1
    # i의 첫번째부터 3번째를 나열
    for i in left_cards:
        # i의 첫번째에서, j의 1~3을 뽑아주고, i의 2,3도 마찬가지.
        for j in right_cards:
            # result값보다 i*j의 값이 크다면, result값에 넣어준다.
            # 그렇게 될 경우, 가장 큰 숫자만 살아남는다.
            if result < i*j:
                result = i*j
    # i의 마지막, j의 마지막까지 돌았을 때, 가장 큰 result값을 반환한다.
    # max_product = max(max_product,i*j)와 같은 말.
    return result


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))


# """ yoonsang """
# def max_product(left_cards, right_cards):
#     # 코드를 작성하세요.
#     answer = 0
#     for i in range(len(left_cards)):
#         for j in range(len(right_cards)):
#             if left_cards[i] * right_cards[j] >= answer:
#                 answer = left_cards[i] * right_cards[j]
#     return answer

# # 테스트
# print(max_product([1, 6, 5], [4, 2, 3]))
# print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
# print(max_product([-1, -7, 3], [-4, 3, 6]))

# """ codeit """

# def max_product(left_cards, right_cards):
#     # 현재까지 최댓값을 담기 위한 변수
#     # 처음에는 임시로 -1로 설정
#     max_product = -1

#     # 가능한 모든 조합을 보기 위한 중첩 반복문
#     for left in left_cards:
#         for right in right_cards:
#             # 현재까지의 최댓값 값과 지금 보고 있는 곱을 비교해서 더 큰 값을 최댓값 변수에 담아준다
#             max_product = max(max_product, left * right)

#     # 찾은 최댓값을 리턴한다
#     return max_product
