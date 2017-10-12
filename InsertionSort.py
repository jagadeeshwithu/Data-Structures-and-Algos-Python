"""
Insertion Sort implementation

Time complexity:  O(n2)
Space complexity: O(1)

"""


def InsertionSort(inputlist):

    for i in range(1, len(inputlist)):
        j = i-1
        while inputlist[j] > inputlist[j+1] and j >= 0:
            inputlist[j], inputlist[j+1] = inputlist[j+1], inputlist[j]
            j -= 1
    return inputlist


if __name__ == "__main__":

        print(InsertionSort([1, 9, 3, 8, 2, 5, 6, 4, 7]))