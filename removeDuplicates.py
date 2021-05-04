
n1 = [1,1,2] # ans 2, n1 = [1,2]
n2 = [0,0,1,1,1,2,2,3,3,4] # ans 5, nums = [0,1,2,3,4]
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums[:] = sorted(set(nums))
    return len(nums)
removeDuplicates(n1)
print(removeDuplicates(n2))