def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    if len(items) < 1:
        return ('No items to sort')
    else:
        n = len(items)
        for i in range(n):
            for j in range(0, n-i-1):
                if items[j] > items[j+1]:
                    items[j], items [j+1] = items[j+1], items[j]

    return items

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

    if len(items) < 1:
        return ('No items to sort')
    else:
        if len(items)>1:
            mid = len(items)//2
            lefthalf = items[:mid]
            righthalf = items[mid:]

            #recursion
            merge_sort(lefthalf)
            merge_sort(righthalf)

            i = 0
            j = 0
            k = 0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    items[k] = lefthalf[i]
                    i += 1
                else:
                    items[k] = righthalf[j]
                    j = j + 1
                k += 1

            while i < len(lefthalf):
                items[k] = lefthalf[i]
                i += 1
                k += 1

            while j < len(righthalf):
                items[k] = righthalf[j]
                j += 1
                k += 1

    return items

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

    if items:
        pivot = items[0]
        # below will be less than pivot point:
        below = [i for i in items[1:] if i < pivot]
        # above will be greater than or equal to pivot point:
        above = [i for i in items[1:] if i >= pivot]
        return quick_sort(below) + [pivot] + quick_sort(above)
    else:
        return items 
