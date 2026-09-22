class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            premap[c].append(p)

        visited=set()

        def dfs(c):
            if c in visited:
                return False
            if premap[c] == []:
                return True
            visited.add(c)
            for p in premap[c]:
                if not dfs(p): return False
            visited.remove(c)
            premap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c) : return False
        return True
        