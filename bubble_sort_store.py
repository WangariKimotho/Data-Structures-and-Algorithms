def bubble_sort_store(elements, key):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j][key] > elements[j+1][key]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        if not swapped:
            break


    # for idx, ele in enumerate(elements):
    #     if key in ele:
    #         swapped = False
    #         for j in range(len(elements)-1-idx):
    #             if elements[idx][key] > elements[idx+1][key]:
    #                 elements[idx], elements[idx+1] = elements[idx+1], elements[idx]
    #                 swapped = True
    #         if not swapped:
    #             break

    #return elements


    # if key in elements[0]:
    #     for i in range(len(elements)-1):
    #         swapped = False
    #         for j in range(len(elements)-1-i):
    #             if elements[key][j] > elements[key][j+1]:
    #                 elements[key][j], elements[key][j+1] = elements[key][j+1], elements[key][j]
    #                 swapped = True
    #             if not swapped:
    #                 break
    #     return elements
    # else:
    #     print("key doesn't exist")
    #     return


if __name__ == "__main__":
    elements = [
        {'name': 'Wanjiku', 'transaction_amount': 457978654, 'device': 'huawei'},
        {'name': 'Mwangi', 'transaction_amount': 342109, 'device': 'samsung'},
        {'name': 'Wangui', 'transaction_amount': 200000, 'device': 'iphone'}
    ]
    bubble_sort_store(elements, 'device')
    print(elements)
