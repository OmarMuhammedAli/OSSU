import random

def randomized_quicksort(array, left=None, right=None):
    if len(array) == 1: return
    if left is None: left = 0
    if right is None: right = len(array) - 1

    def partition(array, left, right):
        count = right - left
        pi = random.randint(left, right)
        # print(pi)
        array[left], array[pi] = array[pi], array[left]
        pivot = array[left]
        i = left + 1
        for j in range(left+1, right+1):
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i += 1
        array[left], array[i - 1] = array[i - 1], array[left]
        return i - 1, count

    count = 0
    if left < right:
        pivot_index, count = partition(array, left, right)
        # print(array)
        count += randomized_quicksort(array, left, pivot_index-1)
        count += randomized_quicksort(array, pivot_index+1, right)
    
    return count

def main():
    with open('quicksort.txt') as fhand:
        samples = [int(line) for line in fhand]
        print('comparisons: ', randomized_quicksort(samples))
        # print(samples[:100])
    # lst = [3, 8, 2, 5, 1, 4, 7, 6]
    # randomized_quicksort(lst)
    # print(lst)

if __name__ == "__main__":
    main()
    