class Node:
	def __init__(self,value):
		self.down=None
		self.up=None
		self.value=value
class stack:
	def __init__(self):
		self.BottomOfStack=None
		self.TopOfStack=None
	def push(self,value,TopOfStack=None):
		if self.BottomOfStack==None:
			self.BottomOfStack=Node(value)
			return

		if TopOfStack==None:
			TopOfStack=self.BottomOfStack

		if TopOfStack.up==None:
			TopOfStack.up=Node(value)
			TopOfStack.up.down=TopOfStack
			self.TopOfStack=TopOfStack.up
			TopOfStack=self.TopOfStack
		else:
			self.push(value,TopOfStack.up)
	def pop(self):
		if self.TopOfStack==None or self.BottomOfStack==None:
			print("Stack is empty")
			return
		if self.TopOfStack.value==None or self.TopOfStack.up==self.BottomOfStack:
			print("Empty Stack")
			return
		if self.TopOfStack==self.BottomOfStack:
			popped=self.TopOfStack.value
			self.TopOfStack=self.TopOfStack.down
			self.BottomOfStack=self.BottomOfStack.down
			return popped
		else:
			popped=self.TopOfStack.value
			self.TopOfStack=self.TopOfStack.down
			self.TopOfStack.up=None
			return popped
		
		
	def ViewAll(self, BottomOfStack=None):
		if self.BottomOfStack==None:
			print("Full Stack: Stack is empty")
			return
		if BottomOfStack==None:
			BottomOfStack=self.BottomOfStack
			print("Full Stack: ",end="=> ")
			print(BottomOfStack.value,end=", ")
		if BottomOfStack.up!=None:
			print(BottomOfStack.up.value,end=", ")
			self.ViewAll(BottomOfStack.up)
		else:
			print()
	def peek(self):
		if self.BottomOfStack!=None:
			return self.BottomOfStack.value
		else:
			return "Stack is empty"
if __name__=="__main__":
	print("###################################################################Stack###################################################################")
	s=stack()
	s.push("Potato")
	print(s.peek())
	s.push("Tomato")
	print(s.pop())
	print(s.pop())
	s.ViewAll()
	print(s.peek())
	s.push("Potatito")
	s.push("Tomatino")
	s.push("I' m Batman")
	print(s.peek())
	s.ViewAll()
    
