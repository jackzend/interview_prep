
s1 = "011101" # ans = 5


def maxScore(s): # o(n) time
    """
    :type s: str
    :rtype: int
    """
    sz = len(s)

    l_array = [1] if s[0] == '0' else [0]
    # fill in l_array
    for i in range(1,sz):
        if s[i] == '0':
            push_val = l_array[-1] + 1
        else:
            push_val = l_array[-1]
        l_array.append(push_val)
    #print(l_array)

    r_array = [1] if s[-1] == '1' else [0]

    for i in range(len(s) - 2,-1, -1):
        if s[i] == '1':
            push_val = r_array[-1] + 1
        else:
            push_val = r_array[-1]
        r_array.append(push_val)

    #print(r_array)
    max_score = 0
    for i in range(0,sz - 1):
        score = l_array[i] + r_array[-1 - (1+i)]
        if score > max_score:
            max_score = score

    return max_score

print(maxScore(s1))
