class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i: [] for i in range(numCourses)}
        for c,p in prerequisites:
            premap[c].append(p)

        visit=set()
        output=[]

        def dfs(c):
            if c in visit:
                return False
            if premap[c] is None:
                return True
            visit.add(c)

            for p in premap[c]:
                if not dfs(p): return False
            visit.remove(c)
            premap[c] = None
            output.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c) : return []
        return output                    