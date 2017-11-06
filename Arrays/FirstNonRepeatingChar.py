"""
Implementing First Non Repeating character from the given array

"""


def firstNotRepeatingCharacter(s):

    count = {}
    for c in s:
        if c not in count:
            count[c] = 0
        count[c] += 1

    for c in s:
        if count[c] == 1:
            return c
        
    return '_'


if __name__ == "__main__":
    print(firstNotRepeatingCharacter('aabaccabad'))