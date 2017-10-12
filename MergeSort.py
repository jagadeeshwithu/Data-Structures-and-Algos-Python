"""
Merge Sort implementation: Recursive way

Time complexity:  O(nlogn)
Space complexity: O(n)


"""


def mergeSort(inputlist):
    arraylen = len(inputlist)
    if arraylen > 1:
        mid = arraylen//2
        left = inputlist[:mid]
        right = inputlist[mid:]

        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                inputlist[k] = left[i]
                i += 1
            else:
                inputlist[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            inputlist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            inputlist[k] = right[j]
            j += 1
            k += 1

        return inputlist


if __name__ == "__main__":

        print(mergeSort([1, 3, 8, 5, 6, 4]))