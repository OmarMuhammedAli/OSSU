

def quicksort(array, left=None, right=None):
    if len(array) == 1: return array
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    
    def median_of_three(array, left, right):
        n = right - left + 1
        mid = (left + right) // 2
        
        if array[left] > array[mid]:
            if array[left] < array[right]:
                return left
            elif array[mid] > array[right]:
                return mid
            else:
                return right
        else:
            if array[left] > array[right]:
                return left
            elif array[mid] < array[right]:
                return mid
            else:
                return right
       

    def partition(array, left, right):
        count = right - left
        #print('count: ', count)
        i = left + 1
        #print('left: ', left, 'right: ', right)
        #array[left], array[right] = array[right], array[left]
        median = median_of_three(array, left, right)
        array[left], array[median] = array[median], array[left]
        pivot = array[left]
        #print('Pivot: ', pivot)
        for j in range(left + 1, right + 1):
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i += 1
        array[left], array[i - 1] = array[i - 1], array[left]
        return i - 1, count
    
    count = 0
    if left < right: 
        partitioned = partition(array, left, right)
        pivot_index = partitioned[0]
        count = partitioned[1]
        
        #print(array)
        count += quicksort(array, left, pivot_index-1)
        count += quicksort(array, pivot_index+1, right)
        #print('Outer count: ', count)
        

    return count
    

        

def main():
    with open('quicksort.txt') as fhand:
        lst = fhand.read().split('\n')
        sample = [int(entry) for entry in lst]
        print('comparisons: ',quicksort(sample))
        # print(sample[:100])
        


if __name__ == "__main__":
    main()
