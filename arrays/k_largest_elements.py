# User function Template for python3

class Solution:
    # Function to return k largest elements from an array.
    def kLargest(self, li, n, k):
        # code here
        result = []
        temp_array = sorted(li)
        print(temp_array)

        """on parcourt la table trié en commençant par le dernier element
        len(li) -1 jusqu'à l'element len(li) - k -1 par pas de -1"""
        for i in range(len(li) - 1, len(li) - k - 1, -1):
            result.append(temp_array[i])

        return result

# {
# Driver Code Starts
# Initial Template for Python 3

t = int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n = li[0]
    k = li[1]
    li = [int(x) for x in input().strip().split()]
    ob = Solution()
    k_largest_list = ob.kLargest(li, n, k)

    for element in k_largest_list:
        print(element, end=' ')
    print('')
# } Driver Code Ends
