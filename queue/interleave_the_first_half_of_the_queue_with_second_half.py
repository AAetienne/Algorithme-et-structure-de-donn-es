from typing import List


class Solution:
    def rearrangeQueue(self, N: int, q: List[int]) -> List[int]:
        middle = N // 2

        list1: List[int] = []
        list2: List[int] = []


        for i in range(middle):
            list1.append(q[i])

        for i in range(middle, N):
            list2.append(q[i])

        # on efface q pour pouvoir la remplir plutard
        q.clear()

        for i in range(middle):
            q.append(list1[i])
            q.append(list2[i])

        return q


# {
# Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        q = IntArray().Input(N)

        obj = Solution()
        res = obj.rearrangeQueue(N, q)

        IntArray().Print(res)

# } Driver Code Ends
