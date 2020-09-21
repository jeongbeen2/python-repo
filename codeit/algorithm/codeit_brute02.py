# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수


def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수


def closest_pair(coordinates):
    list_len = len(test_coordinates)
    result = [coordinates[0], coordinates[1]]
    ranges = distance(test_coordinates[0], test_coordinates[1])

    for i in range(list_len):
        for j in range(i+1, list_len):
            pick1, pick2 = test_coordinates[i], test_coordinates[j]
            distances = distance(pick1, pick2)
            if ranges > distances:
                ranges = distances
                result[0], result[1] = pick1, pick2
    return result


    # 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
