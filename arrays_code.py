# User function Template for python3
import atexit
import io
import sys
import heapq
from collections import defaultdict

"""dans ce code on ne co,sidère pas le k, on precede par
comparaison de l'element qui précède celui qu'o étudie"""

class Solution:

    # Function to return the sorted array.
    def nearlySorted(self, a, n, k):
        # code here
        for i in range(1, n):
            # on prend l'élément à la position i
            key = a[i]
            # on revient un position en arrière
            j = i - 1

            # on commence au premier élément
            # et on le compare avec l'element qui le précède
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key
        return a


# {
# Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(*ob.nearlySorted(a, n, k))

# } Driver Code Ends