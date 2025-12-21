class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        min_freq = [0] * 26
        for ch in words[0]:
            min_freq[ord(ch) - ord('a')] += 1
        for word in words[1:]:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            for i in range(26):
                min_freq[i] = min(min_freq[i], freq[i])
        result = []
        for i in range(26):
            for _ in range(min_freq[i]):
                result.append(chr(i + ord('a')))
        return result
