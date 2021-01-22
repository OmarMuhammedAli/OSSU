def quicksort(array, left=None, right=None):
    if len(array) == 1: return array
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if not left < right: return

    def partition(array, left, right):
        i = left + 1
        print('left: ', left, 'right: ', right)
        pivot = array[left]
        for j in range(left + 1, right + 1):
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i += 1
        array[left], array[i - 1] = array[i - 1], array[left]
        return i - 1
        
        

    pivot_index = partition(array, left, right)
    print(array)
    quicksort(array, left, pivot_index-1)
    quicksort(array, pivot_index+1, right)
    return array


def main():
    print(quicksort([3, 8, 2, 5, 1, 4, 7, 6]))


if __name__ == "__main__":
    main()
