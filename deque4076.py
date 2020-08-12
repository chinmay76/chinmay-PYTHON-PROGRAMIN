class Deque():
    def __init__(self):
    	self.items = ['chinmay']
    def isEmpty(self):
    	return self.items ==[]
    def addFront(self,items):
    	self.items.append(items)
    	
    def addLast(self,items):
    	self.items.insert(0,items)
    
    def removeFront(self):
    	return self.items.pop()
    def removeLast(self):
    	return self.items.pop(0)
    def size(self):
    	return len(self.items)
    def display(self):
    	print(self.items)
D = Deque()
D.addFront('s')
D.addFront('y')
D.addFront('c')
D.addFront('s')
D.addLast(4)
D.addLast(0)
D.addLast(7)
D.addLast(6)
D.display()
D.removeFront()
D.removeLast()
D.display()
