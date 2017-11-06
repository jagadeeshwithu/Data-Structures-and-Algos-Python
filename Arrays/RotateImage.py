"""
Implementation of Rotating an image 90 deg

For e.g.

Input:   [[1,2,3],
         [4,5,6],
         [7,8,9]]

Output:  [[7,4,1],
         [8,5,2],
         [9,6,3]]

"""


def rotateImage(a):
    N = len(a)

    # anti-diagonal mirror
    for i in range(0, N):
        for j in range(0, N - i):
            a[i][j], a[N - 1 - j][N - 1 - i] = a[N - 1 - j][N - 1 - i], a[i][j]

    # horizontal mirror
    for i in range(0, int(N / 2)):
        for j in range(0, N):
            a[i][j], a[N - 1 - i][j] = a[N - 1 - i][j], a[i][j]

    return a


# Solution 2: using 'zip' and 'reversed' in python

def rotateImage1(a):

    return list(zip(*reversed(a)))


if __name__ == "__main__":

    print(rotateImage(
        [[33, 35, 8, 24, 19, 1, 3, 1, 4, 5],
         [25, 27, 40, 25, 17, 35, 20, 3, 19, 3],
         [9, 1, 9, 30, 9, 25, 32, 12, 15, 22],
         [30, 47, 25, 10, 18, 1, 19, 17, 43, 17],
         [40, 46, 42, 34, 18, 48, 29, 40, 31, 39],
         [37, 42, 37, 19, 45, 1, 4, 46, 48, 13],
         [8, 26, 31, 46, 44, 24, 34, 29, 12, 25],
         [45, 48, 36, 12, 33, 12, 4, 45, 22, 37],
         [33, 15, 34, 25, 34, 8, 50, 48, 30, 28],
         [18, 19, 22, 29, 15, 43, 38, 30, 8, 47]]
    ))

    print(rotateImage1([[1,2,3],
                        [4,5,6],
                        [7,8,9]]
                       ))