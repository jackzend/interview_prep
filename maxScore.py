
s1 = "011101" # ans = 5


def maxScore(s): # Naive o(n^2)
    """
    :type s: str
    :rtype: int
    """
    max_score = 0
    for i in range(1,len(s)):

        ls = s[:i]
        rs = s[i:]

        score = ls.count('0') + rs.count('1')

        if score > max_score:
            max_score = score

    return max_score

print(maxScore(s1))
