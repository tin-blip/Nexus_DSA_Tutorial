class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles)//3
        total = 0
        x = len(piles) - 2
        for _ in range (n):
            total += piles[x]
            x -=2
        return total
