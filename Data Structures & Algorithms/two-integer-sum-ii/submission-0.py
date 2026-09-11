class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1

        while left<right:
            currsum=numbers[left] +  numbers[right]
            if currsum<target:
                left+=1
            elif currsum >target:
                right-=1
            else:
                return [left+1,right+1]
