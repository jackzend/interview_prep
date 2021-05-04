
test = 'IV'

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    sum = 0
    i = 0
    while(i < len(s)):
        if s[i] == 'I' and i != len(s) - 1:
            if s[i + 1] == 'V':
                sum += 4
                i += 1
            elif s[i + 1] == 'X':
                sum += 9
                i += 1
            else:
                sum += 1
        elif s[i] == 'X' and i != len(s) - 1:
            if s[i + 1] == 'L':
                sum += 40
                i += 1
            elif s[i + 1] == 'C':
                sum += 90
                i += 1
            else:
                sum += 10
        elif s[i] == 'C' and i != len(s) - 1:
            if s[i + 1] == 'D':
                sum += 400
                i += 1
            elif s[i + 1] == 'M':
                sum += 900
                i += 1
            else:
                sum += 100
        else:
            sum += roman_map[s[i]]
        i += 1
    return sum

print(romanToInt(test))