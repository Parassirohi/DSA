def shell_sort(arr):
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j > 0 and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]
    for elements in tests:
        shell_sort(elements)
        print(elements)
