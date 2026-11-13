class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[]
        heapq.heapify(maxheap)
        for i in stones:
            heapq.heappush(maxheap,-i)
        while len(maxheap)>1:
            if maxheap[0]==maxheap[1]:
                heapq.heappop(maxheap)
                heapq.heappop(maxheap)
            else:
                val1=-heapq.heappop(maxheap)
                val2=-heapq.heappop(maxheap)
                stone=val1-val2
                heapq.heappush(maxheap,-stone)
        return -maxheap[0] if len(maxheap)!=0 else 0      