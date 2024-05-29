'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:

    # Function to find starting point where the truck can start to get through
    # the complete circle without exhausting its petrol in between.
    def tour(self, lis, n):
        # Code here
        index = 0
        petrol = 0
        distance = 0
        diff = 0
        for i in range(n):
            petrol = lis[i][0]
            distance = lis[i][1]
            diff = abs(petrol - distance)
            if diff == 1:
                return i

        return -1

    """def tour(self, lis, n):
        # Code here
        # queue = Queue()
        index = 0
        bool = False
        for items in lis:
            diff = abs(items[0] - items[1])
            if diff == 1:
                # queue.put(items)
                index += 1
                bool = True
        if bool:
            return index
        else:
            return -1
        # return index"""


# {
# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = []
        for i in range(1, 2 * n, 2):
            lis.append([arr[i - 1], arr[i]])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends