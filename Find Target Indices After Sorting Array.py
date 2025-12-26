class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = []
        nums.sort()
        while True:
            if target in nums:
                n.append(nums.index(target))
                nums[nums.index(target)] = 0
            else:
                break
        return n
