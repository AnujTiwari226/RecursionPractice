from typing import List


class Solution:
    def is_sorted(self, nums: List[int]) -> bool:
        if len(nums) in [0, 1]:
            return True
        else:
            result = nums[0] <= nums[1] and self.is_sorted(nums[1:])
            return result


if __name__ == '__main__':
    print(Solution().is_sorted([2,4,8,9,9,15]))

    print(Solution().is_sorted([2,1,8,9,9,15]))
