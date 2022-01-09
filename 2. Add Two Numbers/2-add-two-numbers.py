# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = ListNode()

    def  begin(self):
        return(self.head.next)

    def append(self,value):
        new_val = ListNode(value)
        current = self.head

        while current.next != None:
            current = current.next

        current.next = new_val

    def display(self):
        displayArray = []
        current = self.head
        
        while current != None:
            displayArray.append(current.val)
            current = current.next
        
        print(displayArray)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ListOut = LinkedList()
        ListOut.display()
        # returnOutput = ListNode()
        # intStore = ListNode() 
        carryInt = 0

        while l1 and l2 != None:

            if (l1.val + l2.val) >= 10:
                intStore = (l1.val + l2.val) % 10
                print(intStore)

                carryInt = 1

                ListOut.append(intStore)
            
            elif l1 == None:
                ListOut.append(l2.val)
                
            elif l2 == None:
                ListOut.append(l1.val)
            
            else:
                intStore = (l1.val + l2.val) + carryInt
                print(intStore)

                carryInt = 0

                ListOut.append(intStore)

            print("List 1: " + str(l1.val))
            print("List 2: " + str(l2.val))
            print("Carry: " + str(carryInt))
            ListOut.display()
            # outptArray = outputArray.next
            l1 = l1.next
            l2 = l2.next

        
        return(ListOut.begin())
