'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:

    # Function to find starting point where the truck can start to get through
    # the complete circle without exhausting its petrol in between.
    def tour(self, lis, n):
        # Code here
        """index = 0
        petrol = 0
        distance = 0
        diff = 0
        for i in range(n):
            petrol = lis[i][0]
            distance = lis[i][1]
            diff = abs(petrol - distance)
            if diff == 1:
                return i

        return -1"""

        """fonctionne sur le site mais ne fonctionne pas ici"""

        start = 0
        total_petrol = 0
        total_distance = 0
        current_petrol = 0

        for i in range(n):
            total_petrol += lis[i][0]
            total_distance += lis[i][1]
            current_petrol += lis[i][0] - lis[i][1]
 
            # If current petrol becomes negative, reset start to the next position
            if current_petrol < 0:
                start = i + 1
                current_petrol = 0

        # If total petrol is greater than or equal to total distance, return start index
        if total_petrol >= total_distance:
            return start
        else:
            return -1


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