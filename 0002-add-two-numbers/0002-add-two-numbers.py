# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         
  
        
        returnlist=ListNode()
        head=returnlist
        carry=0

        while l1 or l2 or carry:
            val=0
            if l1:
                val+=l1.val
                l1=l1.next
            if l2:
                val+=l2.val
                l2=l2.next
            val+=carry
            carry=val//10
            digit=val%10
            returnlist.next=ListNode(digit)
            returnlist=returnlist.next
        return head.next
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # returnlist=ListNode()
        # head=returnlist
        # carry=0 
        # while l1 or l2 or carry:
        #     cursum=0
        #     if l1:
        #         cursum+=l1.val
        #         l1=l1.next
        #     if l2:
        #         cursum+=l2.val
        #         l2=l2.next
        #     cursum+=carry
        #     digit=cursum%10
        #     carry=cursum//10
        #     returnlist.next=ListNode(digit)
        #     returnlist=returnlist.next
        # return head.next
            
        
        
#         dummy=ListNode()
#         curr=dummy
        
#         carry=0
#         while l1 or l2 or carry:
#             v1=l1.val if l1 else 0
#             v2=l2.val if l2 else 0
            
            
#             val=v1+v2+carry
#             carry=val//10
#             val=val%10
#             curr.next=ListNode(val)
            
#             curr=curr.next
#             l1=l1.next if l1 else None
#             l2=l2.next if l2 else None
#         return dummy.next
    
    

    