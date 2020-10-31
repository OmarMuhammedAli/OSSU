import random

def mergesort(a, p=None, r=None):
    if p is None: p = 0
    if r is None: r = len(a) - 1
    if p == r:
        return

    # Get mid point q
    q = (p + r) // 2
    mergesort(a, p, q)
    mergesort(a, q + 1, r)
    merge(a, p, q, r)


def merge(a, p, q, r):
    n1, n2 = q - p + 1, r - q
    left, right = a[p: q+1], a[q+1: r+1]
    end = max(left[n1 - 1], right[n2 - 1]) + 1
    left.append(end)
    right.append(end)
    i, j = 0, 0
    for k in range(p, r + 1):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1


def main():
    lst = [5, 6, 8, 1, 4, 3, 10, 2]
    #for i in range(10000):
     #   lst.append(random.randint(0, 1000000))
    mergesort(lst)
    print(lst)


if __name__ == "__main__":
    main()
