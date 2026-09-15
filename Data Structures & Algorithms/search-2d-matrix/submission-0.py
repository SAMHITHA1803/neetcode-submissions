class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in matrix:
            l,r=0,len(x)-1
            while l<=r:
                k=(l+r)//2
                if target == x[k]:
                    return True
                elif target < x[k]:
                    r=k-1
                else:
                    l=k+1
        return False
        