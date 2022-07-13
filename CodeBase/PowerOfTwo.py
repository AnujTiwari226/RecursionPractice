class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print(n)
        if n == 0:
            return False

        result = (n % 2 == 0 and self.isPowerOfTwo(n // 2)) or n == 1
        return result


print(Solution().isPowerOfTwo(int(input("Enter Input"))))
