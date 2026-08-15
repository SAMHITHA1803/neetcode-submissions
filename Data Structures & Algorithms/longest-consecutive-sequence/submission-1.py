class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res=0
        nums.sort()
        current=nums[0]
        count=0
        i=0
        while i < len(nums):
            if current != nums[i]:
                current=nums[i]
                count=0
            while i < len(nums) and nums[i]==current:
                i+=1
            count+=1
            current+=1
            res=max(count,res)
        return res