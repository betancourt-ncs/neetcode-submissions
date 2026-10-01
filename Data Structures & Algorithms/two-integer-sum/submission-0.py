class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, num in enumerate(nums):
            remainder = target - num

            if remainder in h:
                return [h[remainder], i]

            h[num] = i
            
        return []