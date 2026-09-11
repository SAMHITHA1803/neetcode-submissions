class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[-x for x in stones]

        heapq.heapify(maxheap)

        while len(maxheap) >1:
            if maxheap[0]==maxheap[1]:
                heapq.heappop(maxheap)
                heapq.heappop(maxheap)
            else:
                first=-heapq.heappop(maxheap)
                second=-heapq.heappop(maxheap)
                newval=first-second
                heapq.heappush(maxheap,-newval)

        return -maxheap[0] if len(maxheap) == 1 else 0