def count_inversions(array):
    def sort_and_count(array, start=None, end=None):
        count = 0
        if start < end:
            mid = (start + end) // 2
            count += sort_and_count(array, start, mid)
            count += sort_and_count(array, mid+1, end)
            count += merge_and_count(array, start, mid, end)
        return count

    def merge_and_count(array, start, mid, end):
        count = 0
        n1, n2 = mid - start + 1, end - mid
        left, right = array[start:mid+1], array[mid+1:end+1]
        terminator = max(left[n1-1], right[n2-1]) + 1
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
                count += len(left) - i - 1
        return count
    return sort_and_count(array, 0, len(array)-1)
