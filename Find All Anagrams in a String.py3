class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        scount, pcount = defaultdict(int), Counter(p)

        if len(p) > len(s):
            return[]
        for i in range (len(p)):
            scount[s[i]] += 1
            
        ans = []
        if scount == pcount:
            ans.append(0)

        for i in range(len(p), len(s)):
            scount[s[i]] += 1
            scount[s[i - len(p)]] -= 1
            if scount[s[i - len(p)]] == 0:
                del scount[s[i - len(p)]]
            if scount == pcount:
                ans.append(i - len(p) + 1)

        return ans  
