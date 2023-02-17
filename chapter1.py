import math

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

# Iterative version.
# Notes on lists: if i is a list L's index, then i is only valid when 0 <= i < len(L)
# In Python, L[len(L)] is invalid, but L[len(L):] is the empty list.
# If L is an empty list, then L[0] is invalid, but L[:1] is the empty list.
# If L is nonempty, then L[0] is the first element, and L[:1] is a list holding L's first element.
# L + [] = L; L.append([]) adds an empty list to the end of L
# If e is an element, L + e is invalid; L + [e] *returns* L with e added to the end, but doesn't modify it as in L.append(e).
def Merge(c, d):
    """Produces a list made up of the elements of c and d in order"""
    i, j = 0, 0
    result = []

    while i < len(c) and j < len(d):
        if c[i] < d[j]:
            result.append(c[i])
            i += 1
        else:
            result.append(d[j])
            j += 1
    
    # either one of c[i:] or d[j:] is now empty, so we don't need to check which one still has elements
    return result + c[i:] + d[j:]
    
# Examples/Tests
assert Merge([1,3,5,7], [2,4,6,8]) == [1,2,3,4,5,6,7,8]
assert Merge([1,3], [2,4,6,8]) == [1,2,3,4,6,8]
assert Merge([1,3,5,7], [2,4]) == [1,2,3,4,5,7]


# MergeSort with calling MergeRec for the merge funtion
# len(a) >= 0
# a may have repeated elements
def MergeSortRec(a):
    """Sorts the list a"""
    n = len(a)
    if n == 0 or n == 1:
        return a
    mid = math.floor(len(a)/2)
    c = MergeSortRec(a[:mid])
    d = MergeSortRec(a[mid:])
    return MergeRec(c, d)

# Examples/Tests
assert MergeSortRec([]) == []
assert MergeSortRec([1]) == [1]
assert MergeSortRec([6,2,7,2,2,9,22,1]) == [1,2,2,2,6,7,9,22]

# MergeSort with calling Merge for the merge funtion
# len(a) >= 0
# a may have repeated elements
def MergeSort(a):
    """Sorts the list a"""
    n = len(a)
    if n == 0 or n == 1:
        return a
    mid = math.floor(len(a)/2)
    c = MergeSort(a[:mid])
    d = MergeSort(a[mid:])
    return Merge(c, d)

# Examples/Tests
assert MergeSort([]) == []
assert MergeSort([1]) == [1]
assert MergeSort([6,2,7,2,2,9,22,1]) == [1,2,2,2,6,7,9,22]

def Min(a):
    """Returns the smallest element of a"""
    min = a[0]
    for e in a[1:]:
        if e < min:
            min = e
    return min

# Examples/Tests
assert Min([1,2,3]) == 1
assert Min([-1,-2,-3]) == -3
assert Min([0]) == 0

def SelectionSortHelper(a, result):
    if a == []:
        return result
    else:
        result.append(Min(a))
        a.remove(Min(a))
        return SelectionSortHelper(a, result)

def SelectionSortRec(a):
    """Returns a sorted list of the elements of a. Clears a."""
    return SelectionSortHelper(a, [])
        
# Examples/Tests
assert SelectionSortRec([]) == []
assert SelectionSortRec([1]) == [1]
assert SelectionSortRec([6,2,7,2,2,9,22,1]) == [1,2,2,2,6,7,9,22]

