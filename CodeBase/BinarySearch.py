from typing import List


class BinarySearch:
    def binary_search(self, nums: List[int], target: int, s: int, e: int) -> int :
        if s > e:
            return -1
        mid = s + (e - s) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            idx = self.binary_search(nums, target, mid+1, e)
            return idx
        else:
            idx = self.binary_search(nums, target, s, mid-1)
            return idx


if __name__ == '__main__':
    nums = [8, 9, 10, 15, 16, 18, 19, 21, 22]

    print(BinarySearch().binary_search(nums, 21, 0, len(nums)-1))
    print(BinarySearch().binary_search(nums, 8, 0, len(nums)-1))
    print(BinarySearch().binary_search(nums, 106, 0, len(nums)-1))
