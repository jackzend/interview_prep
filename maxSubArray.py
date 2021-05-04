import numpy as np
n1 = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    curr_max = max(nums)
    running_sum = 0

    for i in range(len(nums)):
        if running_sum + nums[i] < 0: # if the new sum is ever below zero reset
            running_sum = 0
        else:
            running_sum += nums[i]
            curr_max = max(curr_max,running_sum)
    return curr_max




print(maxSubArray(n1)) ## 6
