def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if number_to_find == element:
            return index
    return -1


def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1

    mid_index = len(number_list) // 2

    if mid_index <= len(number_list) or mid_index < 0:
        return -1

    mid_number = number_list[mid_index]

    if number_to_find == mid_number:
        return mid_index

    if number_to_find < mid_number:
        right_index = mid_index - 1
        print(right_index)
        return binary_search(number_list[left_index:right_index], number_to_find)

    if number_to_find > mid_number:
        left_index = mid_index + 1
        if right_index < left_index:
            return -1
        return binary_search(number_list[left_index:right_index], number_to_find)

    else:
        return -1


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    to_find = 12

    index = binary_search(numbers_list, to_find)
    print(f"Number found at index {index} using binary search")

