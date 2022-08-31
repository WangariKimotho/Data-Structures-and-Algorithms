def bubble_sort(elements):
    for i in range(len(elements)-1):
        swapped = False
        for j in range(len(elements)-1-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        if not swapped:
            break
    return elements


if __name__ == "__main__":
    elements = [3, 72, 45, 14, 65, 1, 66, 12, 10]

    bubble_sort(elements)
    print(elements)