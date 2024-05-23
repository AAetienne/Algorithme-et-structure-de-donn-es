# User function Template for python3

'''
    :param head: head of unsorted linked list
    :return: head of sorted linkd list

    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''


class Solution:
    # Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        # on verifie que la liste n'est pas vide
        if not head or not head.next:
            return head

        # on divise d'abord la liste en deux parties
        mid = self.getMiddle(head)
        next_mid = mid.next
        mid.next = None

        left_list = self.mergeSort(head)
        right_list = self.mergeSort(next_mid)

        result = self.merge(left_list, right_list)
        return result

    # ici on fusionne deux liste
    def merge(self, list1, list2):
        # vérifions que les listes ne sont pas vides
        if not list1:
            return list2
        if not list2:
            return list1

        # on compare les données et on met les plus petites devant
        # lors de la fusion
        if list1.data <= list2.data:
            final_list = list1
            final_list.next = self.merge(list1.next, list2)
        else:
            final_list = list2
            final_list.next = self.merge(list1, list2.next)

        return final_list

    # cette fonction permet de determiner le milieu d'une liste chainée
    def getMiddle(self, head):
        # on verifie que la liste n'est pas vide
        if not head:
            return head

        # on initialise a et b
        # a etant la liste avant qui parcourt head une case apres l'autre
        # et b la liste qui parcourt deux cases à la fois
        a = head
        b = head
        while b.next and b.next.next:
            a = a.next
            b = b.next.next
        return a


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys


# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# prints the elements of linked list starting with head
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
    t = int(input("t= "))
    for cases in range(t):
        n = int(input("n= "))
        p = LinkedList()  # create a new linked list 'a'.
        nodes_p = list(map(int, input("list= ").strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends
