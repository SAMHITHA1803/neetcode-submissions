class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t: return ""
        count,window ={},{}
        for c in t:
            count[c] = 1+count.get(c,0)

        res=[-1,-1]
        reslength=float("infinity")
        have=0
        need=len(count)
        l=0

        for r in range(len(s)):
            window[s[r]] = 1+window.get(s[r],0)

            if s[r] in count and window[s[r]] == count[s[r]]:
                have+=1
            while have==need:
                if (r-l+1) < reslength:
                    res=[l,r]
                    reslength = (r-l+1)
                
                window[s[l]]-=1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    have-=1

                l+=1
        l,r=res

        return s[l:r+1] if reslength != float("infinity") else ""

