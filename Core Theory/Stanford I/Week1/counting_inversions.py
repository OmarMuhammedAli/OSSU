def sort_and_count(a):
    return _sort_and_count(a, 0, len(a) - 1)

def _sort_and_count(a, p, r):
    count = 0
    if p < r: 
        q = (p + r) // 2

        count += _sort_and_count(a, p, q)
        count += _sort_and_count(a, q+1, r)
        count += merge_and_countsplit(a, p, q, r)

    return count

def merge_and_countsplit(a, p, q, r):
    n1, n2 = q - p + 1, r - q
    print(n1, n2)
    left, right = a[p: q+1], a[q+1: r+1]
    end = max(left[n1 - 1], right[n2 - 1]) + 1
    left.append(end)
    right.append(end)
    i, j = 0, 0
    count = 0
    for k in range(p, r+1):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            count += len(left) - 1 - i 
            j += 1
        
    return count 

def main():
    lst = [100 - i for i in range(100)]
    print(sort_and_count(lst))

if __name__ == "__main__":
    main()

