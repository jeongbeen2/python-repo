def merge(list1, list2):
    if len(list1) <= 1 and len(list2) <= 1:
        if list1 == [] or list2 == []:
            return list1 + list2
        else:
            if list1[0] < list2[0]:
                return list1 + list2
            else:
                return list2 + list1

    mid_idx = len(list1)//2
    div_left = merge(list1[:mid_idx], list1[mid_idx:])
    div_right = merge(list2[:mid_idx], list2[mid_idx:])


# 테스트
# print(merge([1], []))
# print(merge([], [1]))
# print(merge([2], [1]))
# print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
# print(merge([4, 7, 8, 9], [1, 3, 6, 10]))
