class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # we try to place the largest number(n), then n-1, then n-2...
        # 1. find the index of the current target value
        # 2. if it's not at the front(index 0), flip it to the front
        res = []
        n = len(arr)
        for target in range(n, 1, -1):
            idx = arr.index(target)
            if idx == target - 1:
                continue
            if idx != 0:
                res.append(idx + 1)
                arr[:idx + 1] = arr[:idx + 1][::-1]
                # now it's at the front, flip it to its target position
            res.append(target)
            arr[:target] = arr[:target][::-1]
        return res
