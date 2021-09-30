class node:
	def __init__(self,value):
		self.left=None
		self.right=None
		self.value=value
class queue:
	def __init__(self):
		self.head=None
		self.tail=None
	def add(self,value,head=None):
		if self.head==None:
			self.head=node(value)
			return

		if head==None:
			head=self.head

		if head.right==None:
			head.right=node(value)
			head.right.left=head
			self.tail=head.right

		else:
			self.add(value,head.right)
	def remove(self):
		if self.head==None or self.tail==None:
			print("Queue is empty")
			return
		if self.head.value==None or self.head.left==self.tail:
			return
		if self.head==self.tail:
			removed=self.head.value
			self.head=self.head.right
			self.tail=self.tail.right
			return removed
		else:
			removed=self.head.value
			self.head=self.head.right
			self.head.left=None
			return removed
	def peek(self):
		if self.head!=None:
			return self.head.value
		else:
			return "Queue is empty"
	def ViewAll(self,head=None):
		if self.head==None:
			print("Full Queue: Queue is empty")
			return
		if head==None:
			head=self.head
			print("Full Queue: ",end="=> ")
			print(head.value,end=", ")
		if head.right!=None:
			print(head.right.value,end=", ")
			self.ViewAll(head.right)
		else:
			print()
if __name__=="__main__":
	q = queue()
	q.add("Tomato")
	q.add("Potato")
	q.ViewAll()
	print(q.peek())
	print(q.remove())
	print(q.peek())
	print(q.remove())
	q.ViewAll()
	print(q.peek())
