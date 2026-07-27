class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LL:
    def __init__(self, value):
        newNode = node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def insert_head(self, value):
        newNode = node(value)
        if self.head != None:
           newNode.next = self.head
           self.head = newNode
        else: 
            self.head = newNode
            self.tail = newNode
        self.length += 1

    def __repr__(self):
        textToPrint = ""
        p1 = self.head
        while p1 != None:
            textToPrint += f"{p1.value} -> "
            p1 = p1.next
        return textToPrint[:-3]

    def pop_first(self):
        if self.head == None:
            return "List is empty"
        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            value = self.head.value
            prevHead = self.head
            self.head = prevHead.next
            prevHead.next = None
        
        self.length -= 1
        return value
    
    def append(self, value):
        newNode = node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def pop_last(self):
        if self.head == None:
            return "List is empty"
        if self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
        else:
            value = self.tail.value
            p1 = self.head

            while p1.next != self.tail:
                p1 = p1.next
            
            self.tail = p1
            self.tail.next = None
            self.length -= 1
    
    def get(self, pos):
        if pos > self.length or pos < 0:
            return None
        else:
            p1 = self.head
            for i in range(pos):
                p1 = p1.next
            return p1.value
        
    def reverse(self):
            if self.head == None:
                return "Cannot reverse"
            
            before = None
            p1 = self.head
            self.tail = self.head

            while p1 != None:
                next = p1.next
                p1.next = before
                before = p1
                p1 = next

            self.head = before
            return self

    def find_middle_node(self):
        
        middle = self.length // 2

        p1 = self.head
        for i in range(middle):
            p1 = p1.next
        return p1.value
    
    def find_kth_from_end(self, k):
        if k<=0 or k > self.length or self.head == None:
            return None
        
        p1 = self.head
        for i in range(self.length - k):
            p1 = p1.next
        return p1.value
        
    def remove_duplicates(self):
        if self.head == None or self.head == self.tail:
                return "List too small"

        used = []

        p1 = self.head
        before = None

        while p1 != None:
            if p1.value not in used:
                used.append(p1.value)
                before = p1
                p1 = p1.next

            else:
                before.next = p1.next
                p1 = p1.next
        return self
    
    def swap(self, pos1, pos2):
        pass


myList = LL(6)
myList.insert_head(10)
myList.insert_head(2)
myList.insert_head(6)
myList.insert_head(7)
print(myList)

# myList.reverse
print(myList.reverse())

# myList.find_middle_node
print(myList.find_middle_node())

# myList.find_kth_from_end
print(myList.find_kth_from_end(2))

# myList.remove_duplicates
print(myList.remove_duplicates())
