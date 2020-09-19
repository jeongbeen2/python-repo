# Binary Search Algorism


def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(some_list) - 1

    while start_index <= end_index:
        half_index = (start_index + end_index) // 2
        if element == some_list[half_index]:
            return half_index
        elif element < some_list[half_index]:
            end_index = half_index - 1
        else:
            start_index = half_index + 1
    return -1


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
