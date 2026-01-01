class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 1. Convert all numbers to strings for easier concatenation
        # 2. Perform a manual Bubble sort
        # 3. Join the sorted strings
        # 4. Handle edge case: if the list is [0, 0], join gives "00"
        n = len(nums)
        nums_str = [str(x) for x in nums]
        for i in range(n):
            for j in range(0, n - i - 1):
                # custom comparision
                # if "10" + "2" (102) is less than "2" + "10" (210), swap them
                if nums_str[j] + nums_str[j + 1] < nums_str[j + 1] + nums_str[j]:
                    nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]

        result = "".join(nums_str)
        # we only want to return "0"
        return "0" if result[0] == "0" else result
