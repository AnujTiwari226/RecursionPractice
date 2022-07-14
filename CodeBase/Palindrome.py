class Solution:
    def is_palindrome(self, s, i=0):
        if i > len(s) // 2:
            return True
        # print('value of i', i)
        return s[i] == s[len(s)-i-1] and self.is_palindrome(s, i+1)


print(Solution().is_palindrome('malayalam'))
print(Solution().is_palindrome('Nagaland'
                               ''))
