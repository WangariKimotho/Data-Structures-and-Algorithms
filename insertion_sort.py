def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and elements[j] > anchor:
            elements[j+1],elements[j] = elements[j], elements[j+1]
            j -= 1


def insertion_sort_proper(elements):
    '''
    This algorithm takes an anchor element from the idx of the elements[i]
    where i the iteration number. We then compare this anchor element to the element
    on its left. If the anchor element is less than the ele on its right, the anchor ele,
    (now referred to with its index) is replaced with the value on its left. We then move iteratively to the left
    ie the values previously ordered, and do the same replacing until the anchor ele is rightfully placed.

    '''
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >=0 and elements[j] > anchor:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor



if __name__ == "__main__":
    tests = [
        [12, 45, 14, 65, 1, 66, 72, 10, 3],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted_array: {elements}')