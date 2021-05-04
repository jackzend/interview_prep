
n = 20
def isBadVersion(n): # first bad version is 9, rest are also bad
    if n >= 9:
        return True
    return False

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    begin = 1
    end = n # 20
    if n%2 == 0:
        check = n//2
    else:
        check = n//2 + 1 # check will be 10

    while(True):
        if isBadVersion(check): # this is a bad version, we want to check to the left
            if not isBadVersion(check - 1):
                return check
            begin = begin
            end = check - 1
            check = (end - begin + 1) // 2 + begin
        else: # good version, check to the right
            begin = check
            end = end
            check = (end - begin + 1) // 2 + begin
firstBadVersion(51)