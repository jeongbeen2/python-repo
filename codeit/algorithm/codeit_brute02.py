# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수


def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수


def closest_pair(coordinates):
    list_len = len(test_coordinates)
    ranges = distance(test_coordinates[0], test_coordinates[1])
    result = []
    for i in range(list_len):
        for j in range(i+1, list_len):
            if ranges > distance(test_coordinates[i], test_coordinates[j]):
                ranges = distance(test_coordinates[i], test_coordinates[j])
                result.append(test_coordinates[i])
                result.append(test_coordinates[j])
    return result[-2:]

    # 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
