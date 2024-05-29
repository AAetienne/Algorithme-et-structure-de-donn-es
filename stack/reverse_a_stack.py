# User function Template for python3

from typing import List
from sys import maxsize


class Solution:
    def reverse(self, St: List[int]) -> List[int]:
        # code here
        temp_stack = []

        while St:
            temp_stack.append(St.pop())

        for i in temp_stack:
            St.append(i)

        return St

# {
# Driver Code Starts

# Initial Template for Python 3


for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends