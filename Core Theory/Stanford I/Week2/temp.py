def sort_n_count(a):
    p = 0
    r = len(a) - 1
    return _sort_n_count(a, p, r)


def _sort_n_count(a, p, r):
    count = 0
    if p < r:
        q = (p + r) // 2
        count += _sort_n_count(a, p, q)
        count += _sort_n_count(a, q+1, r)
        count += merge(a, p, q, r)
    return count


def merge(a, p, q, r):
    n1, n2 = q - p + 1, r - q
    left, right = a[p:q+1], a[q+1:r+1]
    end = max(left[n1-1], right[n2-1]) + 1
    left.append(end)
    right.append(end)
    count, i, j = 0, 0, 0
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
    lst = [int(line) for line in open('testcases.txt')]
    print(sort_n_count(lst))


if __name__ == "__main__":
    main()