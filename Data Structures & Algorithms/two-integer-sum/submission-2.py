class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indmap=defaultdict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indmap:
                return [indmap[diff] , i]
            indmap[nums[i]] = i
        return []