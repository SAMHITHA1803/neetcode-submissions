class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i:[] for i in range(numCourses)}
        for crs,req in prerequisites:
            pre[crs].append(req)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if pre[crs] == []:
                return True
            
            visit.add(crs)
            for x in pre[crs]:
                if not dfs(x): return False
            visit.remove(crs)
            pre[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True