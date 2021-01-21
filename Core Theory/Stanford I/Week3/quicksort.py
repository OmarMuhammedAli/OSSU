def quicksort(array, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    def partition(array, left, right):
        pivot = array[left]
        i = left + 1
        for j in range(left, right + 1):
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i += 1
        array[left], array[i - 1] = array[i - 1], array[left]

    partition(array, left, right)
    return array


def main():
    print(quicksort([3, 8, 2, 5, 1, 4, 7, 6]))


if __name__ == "__main__":
    main()
