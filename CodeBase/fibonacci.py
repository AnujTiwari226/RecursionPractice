class Solution:
    def fibonacci(self, n):
        if n in [1, 2]:
            return 1
        if n == 0:
            return n
        else:
            result = self.fibonacci(n-1) + self.fibonacci(n-2)
            return result


if __name__ == '__main__':
    sol = Solution()
    num = int(input("Enter the number: "))
    print("Factorial of %d is : %d" %(num, sol.fibonacci(num)))
