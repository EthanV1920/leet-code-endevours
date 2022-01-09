# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        outputArray = []
        # returnOutput = ListNode()
        # intStore = ListNode() 
        carryInt = 0

        while l1 != None:

            if (l1.val + l2.val) >= 10:
                intStore = (l1.val + l2.val) % 10
                print(intStore)

                carryInt = 1

                outputArray.append(intStore)
            
            else:
                intStore = (l1.val + l2.val) + carryInt
                print(intStore)

                carryInt = 0

                outputArray.append(intStore)

            print("List 1: " + str(l1.val))
            print("List 2: " + str(l2.val))
            print("Carry: " + str(carryInt))
            print(outputArray)
            # outptArray = outputArray.next
            l1 = l1.next
            l2 = l2.next

        node3 = ListNode(outputArray[2],None)
        node2 = ListNode(outputArray[1],node3)
        node1 = ListNode(outputArray[0],node2)
        
        # linkedListOut = ListNode(outputArray[0],ListNode(outputArray[1],ListNode(outputArray[2])))

        return(node1)
