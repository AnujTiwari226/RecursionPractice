class Solution:
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            n = n * self.factorial(n-1)
            return n


if __name__ == '__main__':
    sol = Solution()
    num = int(input("Enter the number: "))
    print("Factorial of %d is : %d" %(num, sol.factorial(num)))
