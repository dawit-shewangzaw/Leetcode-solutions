class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.count = 0
        self.n = k
        self.front = None
        self.rear = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        if self.front is None and self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        if self.front is None and self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            if self.front:
                self.front.prev = None
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            if self.rear:
                self.rear.next = None
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.n
        
# class MyCircularDeque:

#     def __init__(self, k: int):
#         self.k = k
#         self.queue = [0] * k
#         self.front = 0
#         self.rear = 0
#         self.size = 0

#     def insertFront(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         self.front = (self.front - 1 + self.k) % self.k
#         self.queue[self.front] = value
#         self.size += 1
#         if self.size == 1:
#             self.rear = self.front
#         return True

#     def insertLast(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         if self.isEmpty():
#             self.queue[self.rear] = value
#         else:
#             self.rear = (self.rear + 1) % self.k
#             self.queue[self.rear] = value
#         self.size += 1
#         return True

#     def deleteFront(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.front = (self.front + 1) % self.k
#         self.size -= 1
#         return True

#     def deleteLast(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.rear = (self.rear - 1 + self.k) % self.k
#         self.size -= 1
#         return True

#     def getFront(self) -> int:
#         return -1 if self.isEmpty() else self.queue[self.front]

#     def getRear(self) -> int:
#         return -1 if self.isEmpty() else self.queue[self.rear]

#     def isEmpty(self) -> bool:
#         return self.size == 0

#     def isFull(self) -> bool:
#         return self.size == self.k
    
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()