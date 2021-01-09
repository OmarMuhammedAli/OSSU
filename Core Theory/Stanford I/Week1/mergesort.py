def merge_sort(array, start=None, end=None):
    if start is None: start = 0
    if end is None: end = len(array) - 1
    if start == end: return

    mid = (start + end) // 2

    merge_sort(array, start, mid)
    merge_sort(array, mid+1, end)
    merge(array, start, mid, end)

    return array

def merge(array, start, mid, end):
    n1, n2 = mid - start + 1, end - mid
    left, right = array[start:mid+1], array[mid+1:end+1]
    terminator = max(left[n1 - 1], right[n2 -1]) + 1
    left.append(terminator)
    right.append(terminator)
    i, j = 0, 0
    for k in range(start, end+1):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1