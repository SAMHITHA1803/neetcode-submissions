class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count={}
        for i in tasks:
            count[i]=count.get(i,0)+1
        maxheap=[-x for x in count.values()]
        heapq.heapify(maxheap)

        q=deque()
        time=0

        while maxheap or q:
            time+=1
            if maxheap:
                newcnt=1+heapq.heappop(maxheap)
                if newcnt:
                    q.append([newcnt,time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time