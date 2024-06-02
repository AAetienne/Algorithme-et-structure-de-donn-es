# User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''


class Solution():
    # Function to sort the given doubly linked list using Merge Sort.
    def sortDoubly(self, head):
        # Your code here
        if head is None or head.next is None:
            return head

        mid = self.getMIddle(head)

        head = self.sortDoubly(head)
        mid = self.sortDoubly(mid)

        return self.mergeDoubly(head, mid)

    def mergeDoubly(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.data < list2.data:
            list1.next = self.mergeDoubly(list1.next, list2)
            list1.next.prev = list1
            list1.prev = None
            return list1
        else:
            list2.next = self.mergeDoubly(list1, list2.next)
            list2.next.prev = list2
            list2.prev = None
            return list2

    def getMIddle(self, head):
        if head is None:
            return head
        slow = head # parcourt la liste lentement
        fast = head # parcourt la liste rapidement
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        """ici on garde la valeur du noeud"""
        temp = slow.next
        slow.next = None
        if temp is None:
            temp.prev = None
        return temp

# {
# Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        ob = Solution()
        llist.head = ob.sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends