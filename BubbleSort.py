"""
Bubble Sort implementation

Time complexity:  O(n2)
Space complexity: O(1)

"""


def BubbleSort(inputlist):

    n = len(inputlist)
    if n <= 1:
        return inputlist

    for i in range(n):
        for j in range(1, n):
            if inputlist[j-1] > inputlist[j]:
                inputlist[j-1], inputlist[j] = inputlist[j], inputlist[j-1]

    return inputlist


if __name__ == "__main__":

        print(BubbleSort([1, 3, 8, 5, 6, 4]))