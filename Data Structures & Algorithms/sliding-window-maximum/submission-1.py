class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        l=r=0
        q=collections.deque()

        for r in range(len(nums)):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            

            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1

            if l>q[0]:
                q.popleft()
        return output
