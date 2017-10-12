"""
Quick Sort implementation: Recursive way

Time complexity:  O(nlogn) and worst O(n2)
Space complexity: O(n)

The logic implemented here takes the 'pivot' value as the first element in the given input list

"""


def QuickSort(alist):
    quicksorthelper(alist, 0, len(alist)-1)

    return alist


def quicksorthelper(alist, first, last):
    if first < last:
        splitpos = partition(alist, first, last)

        quicksorthelper(alist, first, splitpos-1)
        quicksorthelper(alist, splitpos+1, last)


def partition(alist, first, last):

    pivotvalue = alist[first]

    left = first + 1
    right = last

    done = False
    while not done:

        while left <= right and alist[left] <= pivotvalue:
            left += 1

        while alist[right] >= pivotvalue and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]


    alist[first], alist[right] = alist[right], alist[first]

    return right


if __name__ == "__main__":

        print(QuickSort([9, 10, 1, 3, 7, 8, 5, 6, 4, 2]))