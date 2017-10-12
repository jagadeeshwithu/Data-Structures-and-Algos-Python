"""
Selection Sort implementation

Time complexity:  O(n2)
Space complexity: O(1)

"""


def SelectionSort(inputlist):

    n = len(inputlist)
    if n <= 1:
        return inputlist

    for i in range(n):
        ptr = i
        for j in range(i, n):
            if inputlist[j] < inputlist[ptr]:
                ptr = j
        inputlist[i], inputlist[ptr] = inputlist[ptr], inputlist[i]

    return inputlist


if __name__ == "__main__":

        print(SelectionSort([1, 3, 8, 5, 6, 4]))