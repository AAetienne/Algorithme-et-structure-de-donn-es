# User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''


class Solution:

    # cette fonction permet de trier la liste en faisant appel
    # à la fonction d'insertion
    def insertionSort(self, head):
        # onn verifie si la liste est vide
        if head is None:
            return head

        # liste triée
        sortedlist = None

        # on affecte la liste à une variable
        curr = head

        """tant que la liste n'est pas vide on insert la valeur courante dans
        la liste sortedList en faisant appel à la fonction
        sortedInsert qui insert la valeur envoyée à la position qu'il
        faut par une suite de comparaison"""

        while curr is not None:
            next_node = curr.next
            sortedlist = self.sortedInsert(sortedlist, curr)
            curr = next_node

        return sortedlist

    def sortedInsert(self, sortedHead, new_node):
        # Si la liste triée est vide ou si le nouvel élément doit être inséré en tête
        if sortedHead is None and sortedHead.data >= new_node.data:
            new_node.next = sortedHead
            sortedHead = new_node
        else:
            curr = sortedHead
            while curr.next is not None and curr.next.data < new_node.data:
                curr = curr.next

            new_node.next = curr.next
            curr.next = new_node

        return sortedHead


# {
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
INF = float("inf")


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = Node(INF)
        nodes = list(map(int, input().strip().split()))
        ptr = a
        for x in nodes:
            ptr.next = Node(INF)
            ptr = ptr.next
            ptr.data = x
        a = a.next
        ob = Solution()
        head = ob.insertionSort(a)
        printList(head)
# } Driver Code Ends