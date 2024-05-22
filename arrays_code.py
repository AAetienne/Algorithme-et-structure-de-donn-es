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
        tas = []
        result = []

        """on traite les k+1 premiers elements du tableau
        la fonction heapq.heappush trie le tableau et met les petits
        elements devant et les grands après"""
        for i in range(min(k + 1, n)):
            heapq.heappush(tas, a[i])

        # maintenant on traite les autres elements du tableau
        # de k+1 à n
        for i in range(k + 1, n):
            heapq.heappush(tas, a[i])

            # ensuite on vide le tas
            # le tas est vidé en commençant par le plus petit
        while tas:
            result.append(heapq.heappop(tas))

        return result


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