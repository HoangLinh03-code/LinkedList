class Node:
    def __init__(self, val = 0, next = None):
        self.val  = val
        self.next = next
class Solu:
    def __init__(self) -> None:
        self.head = None

    def clear(self):
        """Clear the entire linked list."""
        self.head = None
    
    def addToList(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return 
        last  = self.head
        while last.next:
            last = last.next
        last.next = newNode

    # def __str__(self) -> str:
    #     # linkList = ""
    #     # temp = self.head
    #     # while temp:
    #     #     linkList += str(temp.val) + "->"
    #     #     temp = temp.next
    #     # return linkList + 'NULL'
    #     node = self.head  # Start from the head of the linked list
    #     result = []  # List to collect string representations of node data
        
    #     while node is not None:  # Traverse until the end of the list
    #         result.append(str(node.val))  # Append the data as a string
    #         node = node.next  # Move to the next node
        
    #     return " -> ".join(result)
    
    def print(self):
        if self.head is None:
            return
        itr = self.head
        temp = []
        while itr:
            temp.append(itr.val)
            itr = itr.next
        return temp
    def OddEvenList(self):
        if self.head is None:
            return
        a = self.head
        b = c = self.head.next
        while b and b.next:
            a.next = b.next
            a = a.next
            b.next = a.next
            b = b.next
        a.next = c
        return self.head

    def delMid(self):
        if self.head is None or next is None:
            return
        slow = self.head
        fast = self.head
        prev  =None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return self.head
    
    def reList(self):
        if self.head is None:
            return None
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev
        return prev
    
    def count(self):
        if self.head is None:
            return
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def pairSum(self):
        if self.head is None:
            return 
        slow, fast = self.head, self.head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        def reverse(head): #Reverse other half
            dummy = Node()
            cur = self.head
            while cur:
                next = cur.next
                cur.next = dummy.next
                dummy.next = cur
                cur = next
            return dummy.next
        pa,q = self.head, slow.next
        slow.next = None # # Break the list into two halves
        pb = reverse(q)
        ans = 0
        while pa and pb:
            ans = max(ans, pa.val + pb.val)
            pa = pa.next
            pb = pb.next
        return ans
    