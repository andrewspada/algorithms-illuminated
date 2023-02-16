import math

def MergeSort(a):
    n = len(a)
    if n == 0 or n == 1:
        return a
    mid = math.floor(len(a)/2)
    c = MergeSort(a[:mid])
    d = MergeSort(a[mid:])
    return MergeRec([], c, d)

# c and d are sorted
# len(c) > 0 and len(d) > 0
# len(c) may be > len(d) and vice versa

def MergeRec(c, d):
    """Produces a list made up of the elements of c and d in order"""
    return MergeRecHelper([], c, d)

def MergeRecHelper(b, c, d):
    if not c:
        return b + d
    elif not d:
        return b + c
    else:
        if c[0] < d[0]:
            return MergeRecHelper(b + [c[0]], c[1:], d)
        else:
            return MergeRecHelper(b + [d[0]], c, d[1:])

# Examples/Tests:
assert MergeRec([1,3,5,7], [2,4,6,8]) == [1,2,3,4,5,6,7,8]
assert MergeRec([1,3], [2,4,6,8]) == [1,2,3,4,6,8]
assert MergeRec([1,3,5,7], [2,4]) == [1,2,3,4,5,7]
