# User function Template for python3
class Solution:

    def count(self, arr, n, x):
        # code here
        number = 0
        # on compte le nombre d'occurence de l'element en incrementant
        # une variabble initialement à 0
        for i in range(n):
            if arr[i] == x:
                number += 1
        return number

# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends
