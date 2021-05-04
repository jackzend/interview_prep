
s1 = "()" # TRUE
s2 = "()[]{}" # TRUE
s3 = "(]" # False
s4 = "([)]" # False
s5 = "(){}}{"

def isValid(s): #o(n) linear time constant
    """
    :type s: str
    :rtype: bool
    """
    matching_brackets = {'(': ')', '[': ']', '{': '}'}

    stack = [] # push is append() pop is pop() top is stack[-1]
    stack.append(s[0])

    if stack[-1] not in matching_brackets.keys(): # we don't start with an openning bracket
        return False

    for i in range(1,len(s)):
        p = s[i]
        if p in matching_brackets.keys(): # if p is new opener
            stack.append(p)
        elif len(stack) == 0 and p not in matching_brackets.keys():
            return False
        elif matching_brackets[stack[-1]] == p: # elif p closes top bracket
            stack.pop()
        else: # p is a non matching closing bracket
            return False

    if len(stack) == 0:
        return True
    return False

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))
print(isValid(s4))
print(isValid(s5))

