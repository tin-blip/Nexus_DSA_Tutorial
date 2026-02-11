class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        check = set()
        maxlen = 0

        for i in range(len(s)):
            while s[i] in check:
                check.remove(s[left])
                left += 1
            check.add(s[i])
            maxlen = max(maxlen, i - left + 1)

        return maxlen
