"""
Get All Permutations of a given string

For e.g. Input: abc
         Output: {bca, acb, abc, cba, bac, cab}
"""


# Solution 1: Using the python library for permutations
from itertools import permutations

perms = [''.join(p) for p in permutations('ALABA')]

res_perms = set(perms)
print(res_perms)
print(len(res_perms))


# List all the permutations from the given range
perms = list(permutations(range(1, 4)))
print(perms)


# Solution 2:
# Time: O(n * n!)
# Space: O(n)
#
# For e.g., [1, 2, 3] have the following permutations:
# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2] and [3, 2, 1].
#

class Solution(object):
    def permute(self, num):
        result = []
        used = [False] * len(num)
        self.permuteRec(result, used, [], num)
        return result

    def permuteRec(self, result, used, cur, num):
        if len(cur) == len(num):
            result.append(cur + [])
            return
        for i in range(len(num)):
            if not used[i]:
                used[i] = True
                cur.append(num[i])
                self.permuteRec(result, used, cur, num)
                cur.pop()
                used[i] = False


print(Solution().permute(range(1,4)))


# Solution 3
# Time: O(n)
# Space: O(1)

class Solution(object):
    def findPermutation(self, s):
        """
        :param s: str
        :return: List[int]
        """

        result = []
        for i in range(len(s)+1):
            if i == len(s) or s[i] == 'I':
                result += range(i+1, len(result), -1)
        return result


print(Solution().findPermutation('abc'))