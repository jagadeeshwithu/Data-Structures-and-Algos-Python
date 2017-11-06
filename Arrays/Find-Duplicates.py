"""
Return the frequencies of elements in the given array

"""


def count_freq(A):
    res = {}

    for i in range(0, len(A)):
            if A[i] not in res:
                res[A[i]] = 1
            elif A[i] in res:
                res[A[i]] += 1

    return res


if __name__ == "__main__":

        result = count_freq([2, 3, 3, 2, 5, 6, 7, 6, 7, 6, 7, 7, 7, 5, 2])
        for key, val in result.items():
            print("{} : {}".format(key, val))
