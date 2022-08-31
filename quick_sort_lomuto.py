def swap(elements, a, b):
    if a != b:
        elements[a], elements[b] = elements[b], elements[a]


def partition(elements, start, end):
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(elements, i, p_index)
            p_index += 1

    swap(elements, p_index, end)
    return p_index


def quick_sort(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)


if __name__ == "__main__":
    elements = [11, 6, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

