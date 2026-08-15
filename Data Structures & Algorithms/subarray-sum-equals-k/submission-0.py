class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        prefix = {0:1}
        currprefixsum=0
        for x in nums:
            currprefixsum+=x
            diff = currprefixsum - k

            res+=prefix.get(diff,0)

            prefix[currprefixsum]=1+prefix.get(currprefixsum,0)

        return res
