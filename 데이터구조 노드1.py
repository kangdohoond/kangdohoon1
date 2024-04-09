# # class Node:
# #   def __init__(self, item, next=None, prev=None):
# #     self.item = item
# #     self.next = None
# #     self.prev = None

# # class LinkedList:
# #   def __init__(self):
# #     self.head = None

# #   def insert(self, i:int, x:int):
# #     """insert x in ith element"""

# #   def delete(self, i):

# #     """delete ith element"""

# #   def printList(self):
# #     """여기에 코딩"""
# #     #self.head =1
# #     # self.newNode = self.head.next
# #     self.head = 1
# #     cur = self.head

# #     while cur is not None:
# #         print(f"cur : {cur}, end = " " ")
# #         cur = cur.next
# #     cur.next = self.prev
# # a = LinkedList()
# # a.printList()
        


# # class Node:
# #     def __init__(self, item, next=None, prev=None):
# #         self.item = item
# #         self.next = next
# #         self.prev = prev

# # class LinkedList:
# #     def __init__(self):
# #         self.head = None

# #     # def insert(self, i:int, x:int):
# #     #     """insert x in ith element"""
# #     #     pass  # 구현 필요

# #     def delete(self, i):
# #         """delete ith element"""
# #         pass  # 구현 필요

# #     def printList(self):
# #         """print the linked list"""
# #         cur = self.head
# #         while cur is not None:
# #             print(cur.item, end="")
# #             if cur.next is not None:  # 다음 노드가 None이 아닌 경우에만 "->"를 출력합니다.
# #                 print(" -> ", end="")
# #             cur = cur.next
# # # class SingleLinkedList(LinkedList):
# # #   def __init__(self):
# # #     super().__init__()
# # #     self.head = Node(None)
# # #     self.dummy = Node(None, self.head)
# # #     self.head.next = self.dummy

# # #   def insert(self, i:int, x:int):
# # #     newNode = Node(x)  # 새로운 노드 생성 
# # #     current = self.head  # 첫 노드
# # #     while i != -1:  # i 가 -1이 될 때까지 반복 , 즉
# # #       # i 까지 현재 노드를 이동시키는 중, 1 이라면 2번째 노드로 이동
# # #       current = current.next # 현재 노드를 다음 노드로 이동시킴
# # #       i -= 1  # 결국 current는 맨 마지막 노드
# # #     newNode.next = current.next
# # #     current.next = newNode  # currnt 다음 노드는 항상 newNode
# # class SingleLinkedList(LinkedList):
# #     def __init__(self):
# #         super().__init__()
# #         self.head = Node(None)
# #         self.dummy = Node(None, self.head)
# #         self.head.next = self.dummy

# #     def insert(self, i:int, x:int):
# #         newNode = Node(x)  
# #         current = self.head  
# #         while i != -1:  # -1이 될 때까지 반복
# #             current = current.next  
# #             i -= 1  
# #         newNode.next = current.next
# #         current.next = newNode

# #     def reverse(self):
# #         pr = None
# #         curr = self.head
# #         while curr is not None: # 결국 curr = None 이 됨 언젠가는
# #             ne1 = curr.next  # 다음 노드 저장   , 존나 헷갈리는데 이 코드는 curr.next가 진짜 생긴게아니라 , 그냥 단순 변수에 저장한 것 뿐 . 저장만 !!! 
# #             #  단순 변수에 값 저장만 한 거지 

# #             curr.next = pr  # 현재 노드의 다음 노드를 이전 노드로 변경 
            
# #             pr = curr       # 이전 노드를 현재 노드로 변경 , 즉 99줄 , 100줄이 있기때문에 pr이 이전노드라는 걸 알 수 있음
# #             curr = ne1      # 현재 노드를 다음 노드로 변경

# #         self.head = pr
# #         # return pr

# # a = SingleLinkedList()
# # a.head = Node(1)
# # a.head.next = Node(2)
# # a.head.next.prev = a.head
# # a.head.next.next = Node(3)
# # # a.insert(1,3)
# # a.head.next.next.prev = a.head.next
# # a.head.next.next.next = Node(4)
# # a.head.next.next.next.next = Node("end")

# # a.printList() 
# # print("\n")
# # a.reverse()
# # a.printList() 




class Node:
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next  #
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
    

    def insert(self, i:int, x:int):
         """insert x in ith element"""
         pass  # 구현 필요

    def delete(self, i):
        """delete ith element"""
        pass  # 구현 필요

    def printList(self):
        """print the linked list"""
        cur = self.head
        while cur is not None:
            print(cur.item, end="")
            if cur.next is not None:  # 다음 노드가 None이 아닌 경우에만 "->"를 출력합니다.
                print(" -> ", end="")
            cur = cur.next

class SingleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.head = Node(None)
        self.dummy = Node(None, self.head)
        self.head.next = self.dummy

    def insert(self, i:int, x:int):
        newNode = Node(x)  
        current = self.head  
        while i != -1:  # -1이 될 때까지 반복
            current = current.next  
            i -= 1  
        newNode.next = current.next
        current.next = newNode

    def reverse(self):
        pr = None
        curr = self.head
        while curr is not None: # 결국 curr = None 이 됨 언젠가는
            ne1 = curr.next  # 다음 노드 저장   , 존나 헷갈리는데 이 코드는 curr.next가 진짜 생긴게아니라 , 그냥 단순 변수에 저장한 것 뿐 . 저장만 !!! 
            #  단순 변수에 값 저장만 한 거지 

            curr.next = pr  # 현재 노드의 다음 노드를 이전 노드로 변경 // 질문 : while 두번쨰 루프에서 curr.next = None이 왜 아닌지 . 
            
            pr = curr       # 이전 노드를 현재 노드로 변경 , 즉 99줄 , 100줄이 있기때문에 pr이 이전노드라는 걸 알 수 있음
            curr = ne1      # 현재 노드를 다음 노드로 변경

        self.head = pr
        # return pr

a = SingleLinkedList()
a.head = Node(1)
a.head.next = Node(2)
a.head.next.prev = a.head
a.head.next.next = Node(3)

a.head.next.next.prev = a.head.next
a.head.next.next.next = Node(4)
a.head.next.next.next.next = Node("end")

a.printList() 
print("\n")
a.reverse()
a.printList() 






# class Node:
#     def __init__(self, item, next=None, prev=None):
#         self.item = item
#         self.next = next  #
#         self.prev = prev

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self

#     def insert(self, i:int, x:int):
#          """insert x in ith element"""
#          pass  # 구현 필요

#     def delete(self, i):
#         """delete ith element"""
#         pass  # 구현 필요

#     def printList(self):
#         """print the linked list"""
#         cur = self.head
#         while cur is not None:
#             print(cur.item, end="")
#             if cur.next is not None:  # 다음 노드가 None이 아닌 경우에만 "->"를 출력합니다.
#                 print(" -> ", end="")
#             cur = cur.next

# class SingleLinkedList(LinkedList):
#     def __init__(self):
#         super().__init__()
#         self.head = Node(None)
#         self.dummy = Node(None, self.head)
#         self.head.next = self.dummy

#     def insert(self, i:int, x:int):
#         newNode = Node(x)  
#         current = self.head  
#         while i != -1:  # -1이 될 때까지 반복
#             current = current.next  
#             i -= 1  
#         newNode.next = current.next
#         current.next = newNode

#     # def reverse(self):
#     #     pr = None
#     #     curr = self.head
#     #     while curr is not None: # 결국 curr = None 이 됨 언젠가는
#     #         ne1 = curr.next  # 다음 노드 저장   , 존나 헷갈리는데 이 코드는 curr.next가 진짜 생긴게아니라 , 그냥 단순 변수에 저장한 것 뿐 . 저장만 !!! 
#     #         #  단순 변수에 값 저장만 한 거지 

#     #         curr.next = pr  # 현재 노드의 다음 노드를 이전 노드로 변경 
            
#     #         pr = curr       # 이전 노드를 현재 노드로 변경 , 즉 99줄 , 100줄이 있기때문에 pr이 이전노드라는 걸 알 수 있음
#     #         curr = ne1      # 현재 노드를 다음 노드로 변경

#     #     self.head = pr
#     #     # return pr
#     def reverse(self):
#         current = self.head.next.next.next
#         if current.prev is None:
#             print("Warning: Data Empty....")
#             return

#         print("Reverse Data List")
#         while current is not None:
#             if current.item is not None:
#                 print(current.item, end = " >> ")
#             current = current.prev

#         print("[None]")
# a = SingleLinkedList()
# a.head = Node(1)
# a.head.next = Node(2)
# a.head.next.prev = a.head
# a.head.next.next = Node(3)

# a.head.next.next.prev = a.head.next
# a.head.next.next.next = Node(4)
# a.head.next.next.next.next = Node("end")

# a.printList() 
# print("\n")
# a.reverse()
# #a.printList()



