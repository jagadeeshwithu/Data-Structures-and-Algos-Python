"""
Implementation for finding First Duplicate in the list
"""


def firstDuplicate(a):

    res = {}

    for i in range(0, len(a)):
        if a[i] not in res:
            res[a[i]] = 1

        elif a[i] in res:
            return a[i]

    return -1


if __name__ == "__main__":

    print(firstDuplicate([2, 3, 1, 5, 5, 2]))