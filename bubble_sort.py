def bubble_sort(elements):
    size = len(elements)

    for j in range(size-1):
        swapped = False
        for i in range(size-1):
            if elements[i] > elements[i+1]:
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    elements2 = [1, 2, 3, 4, 2]
    elements3 = ["mona", "dhaval", "aamir", "tina", "chang"]
    bubble_sort(elements)
    bubble_sort(elements2)
    bubble_sort(elements3)

    print(elements)
    print(elements2)
    print(elements3)

