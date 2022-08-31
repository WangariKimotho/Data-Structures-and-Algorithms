def merge_sort(elements, key, descending=True):
    '''
    Function that uses the divide and conquer to recursively sort elements.
    Args: elements array inputs, tested types are int, float and string
            array elements.
            key: assumes a dictionary structure hence the key is the
            tag to sort the elements by.
            descending:boolean True or False, will only be used when calling
            the merge_sorted_arrays function.
    Returns: arrays divided into the smallest surest sorted form, ie one element. Then these arrays
            are passed to the merge_sorted_array function.
    '''

    if len(elements)<=1:
        return
    mid = len(elements)//2
    left = elements[:mid]
    right = elements[mid:]
    merge_sort(left,key)
    merge_sort(right,key)
    merge_sorted_array(left,right,elements,key,descending)


def merge_sorted_array(a,b,arr,key,descending=False):
    '''
    Takes 2 already sorted arrays and merges their elements
    to return a sorted list. The key assumes that the data is stored in
    dictionary format hence the input key is the element to sort the
    arrays by. By default, descending is False.
    Args: a,b sorted array inputs.
           key from a dictionary data structure by which to sort by.
           descending, boolean, True or False, default False.

    Return: sorted array.

    '''
    i=j=k=0
    if descending:
        while i < len(a) and j < len(b):
            if a[i][key] >= b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1
        while i < len(a):
            arr[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            arr[k] = b[j]
            j += 1
            k += 1
    else:
        while i < len(a) and j < len(b):
            if a[i][key] < b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1
        while i < len(a):
            arr[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            arr[k] = b[j]
            j += 1
            k += 1


if __name__ =="__main__":
    elements = [
        {'name':'vedanth', 'age':7,'time_hours':1},
        {'name':'rajab','age':20,'time_hours':3},
        {'name':'vigmesh','age':54,'time_hours':2.5},
        {'name': 'kamudu', 'age': 9, 'time_hours': 0.9},
        {'name':'kimosh','age':5, 'time_hours':1.2}
        #17,2,21,9,25=> 25,21,17,9,2
    ]
    merge_sort(elements,key='age',descending=True)
    print(elements)