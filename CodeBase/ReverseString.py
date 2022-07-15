from typing import List


class Solution:
    def reverseString(self, s: List[str], idx=0) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse_inplcae(s=s, start=0, end=len(s)-1)

    def reverse_inplcae(self, s, start, end):
        while start >= end:
            return
        s[start], s[end] = s[end], s[start]
        self.reverse_inplcae(s, start+1, end-1)


st = ["h","e","l","l","o"]
Solution().reverseString(st)
print(st)
