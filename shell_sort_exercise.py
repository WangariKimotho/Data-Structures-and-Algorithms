def shell_sort(arr):
    ''''
    This function is an extension of the shell sort algorithm which besides sorting
    using the shell sort method, also removes elements that appear more than once.
    In its current form it only removes duplicates appearing twice and may fail if the
     duplicate appears more than twice.
     Takes in an array, and returns a sorted array.
    '''
    size= len(arr)
    gap = size//2

    while gap > 0:
        i=gap
        removed = False
        while i >=gap and i < size:
        #for i in range(gap, size):
            anchor = arr[i]
            j=i
            while j >= gap and arr[j-gap] >= anchor:
                if arr[j-gap]==anchor:
                    arr.remove(arr[j-gap])
                    removed = True
                    j -= 1

                else:
                    arr[j] = arr[j-gap]
                    j -= gap
               # size=len(arr)
            arr[j] = anchor
            if removed:
                size = len(arr)
            i+=1


        gap = gap //2

if __name__ =="__main__":
    tests = [
       [12, 45, 14, 65, 1, 66, 72, 14, 10,10, 3],
        [3, 7, 9,9, 11],
        [25,10, 22, 21,10,10],
        [29, 15, 28,29],
        [],
        [6]
    ]
    for elements in tests:
        shell_sort(elements)
        print(elements)