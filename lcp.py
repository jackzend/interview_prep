s1 = "leetscode"
s2 = "lts"

def lcp_two_strings(s1, s2):

    n1 = len(s1)
    n2 = len(s2)

    lcp = ""

    for i in range(0,min(n1,n2)):
        if s1[i] == s2[i]:
            lcp = s1[0:i+1]
        else:
            return lcp
    return lcp

strings = ["flower","flow","flight"] # ans = fl
strings1 = ["dog","racecar","car"] # ans = ""
def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        lcps = strs

        while(len(lcps) != 1):
            lcp = lcp_two_strings(lcps[0],lcps[1])
            lcps.append(lcp)
            del lcps[0:2]


        return lcps[0]

print(longestCommonPrefix(strings))
print(longestCommonPrefix(strings1))
