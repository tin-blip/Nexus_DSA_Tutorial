class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        n = len(words)
        # pre-convert strings to sets so we don't do it repeatedly in the loop
        word_sets = [set(w) for w in words]
        # compare every pair (i, j) where i < j
        for i in range(n):
            for j in range(i + 1, n):
                if word_sets[i] == word_sets[j]:
                    count += 1
        return count
