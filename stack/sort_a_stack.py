class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        temp_Stack = []
        while s:
            temp_value = s.pop()

            while temp_Stack and temp_Stack[-1] < temp_value:
                s.append(temp_Stack.pop())

            temp_Stack.append(temp_value)

        while temp_Stack:
            s.append(temp_Stack.pop())


#{
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends