from queue import PriorityQueue

n1 = [1,2,0]
def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s = set(nums)
    pq = PriorityQueue()
    for n in s:
        pq.put(n)
    i = 1
    while not pq.empty():
        top = pq.get()

        if top <= 0:
            continue
        elif top == i:
            i += 1
        else:
            return i
    return i

print(firstMissingPositive(n1))