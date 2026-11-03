class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in matrix:
            l,r=0,len(i)-1
            while l<=r:
                m=(l+r)//2
                if target == i[m]:
                    return True
                elif target < i[m]:
                    r=m-1
                else:
                    l=m+1
        return False
