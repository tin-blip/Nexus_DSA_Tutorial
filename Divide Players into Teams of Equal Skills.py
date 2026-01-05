class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        n = len(skill)
        target_sum = skill[0] + skill[-1]
        total_chemistry = 0
        for i in range (n//2):
            left_player = skill[i]
            right_player = skill[n-1-i]
            if left_player + right_player != target_sum:
                return -1
            total_chemistry += (left_player * right_player)
        return total_chemistry
