class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        for i in nums:
            count[i]+=1
        f=[[] for i in range(len(nums)+1)]
        for num,freq in count.items():
            f[freq].append(num)
        res=[]
        for i in range(len(f)-1,0,-1):
            for num in f[i]:
                res.append(num)
                if len(res)==k:
                    return res