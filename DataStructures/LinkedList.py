class Node:
	def __init__(self,value):
		self.left=None
		self.right=None
		self.value=value
class LinkedList:
	def __init__(self):
		self.head=None
		self.tail=None
	def insertend(self,value,head=None):
		if self.head==None:
			self.head=Node(value)
			return

		if head==None:
			head=self.head

		if head.right==None:
			head.right=Node(value)
			head.right.left=head
			self.tail=head.right

		else:
			self.insertend(value,head.right)

	def inserthead(self,value):
		if self.head==None:
			self.head=Node(value)
		else:
			head=self.head
			head.left=Node(value)
			head.left.right=head
			self.head=head.left
	def insertafter(self,value_after,value,head=None):
		if self.head==None:
			print("The list is Null, so value absent")
			return
		if head==None:
			head=self.head
		if head.value==value_after:
			temp=head.right
			head.right=Node(value)
			head.right.right=temp
			head.right.left=head
			temp.left=head.right
		elif head.right!=None:
			self.insertafter(value_after,value,head.right)
		else:
			print("value not in list")
	def insertbefore(self,value_before,value,head=None):
		if self.head==None:
			print("The list is Null, so value absent")
			return
		if head==None:
			head=self.head
		if head.value==value_before:
			temp=head.left
			head.left=Node(value)
			head.left.left=temp
			head.left.right=head
			temp.right=head.left
		elif head.right!=None:
			self.insertbefore(value_before,value,head.right)
		else:
			print("value not in list")

	def inorder(self, head=None):
		if head==None:
			head=self.head
			print("Inorder",end="=> ")
			print(head.value,end=", ")
		if head.right!=None:
			print(head.right.value,end=", ")
			self.inorder(head.right)
		else:
			print() #The Empty print statement(after the method) ensures that the next print statement is printed in the next line

	def postorder(self, tail=None):
		if tail==None:
			tail=self.tail
			print("Postorder",end="=> ")
			print(tail.value,end=", ")
		if tail.left!=None:
			print(tail.left.value,end=", ")
			self.postorder(tail.left)
		else:
			print()#The Empty print statement(after the method) ensures that the next print statement is printed in the next line
			
	def delete(self,value,head=None):
		if self.head==None:
			print("The list is Null")
			return
		if head==None:
			head=self.head
		if head.value==value:
			temp=head
			head.right.left=head.left
			temp.left.right=temp.right
			temp=None #Unnecessary but frees memory, that's what i thought

		elif head.right!=None:
			self.delete(value,head.right)
		else:
			print("value not in list")
	def update(self,initial_val,final_val,head=None):
		if self.head==None:
			print("The list is Null")
			return
		if head==None:
			head=self.head
		if head.value==initial_val:
			head.value=final_val
		elif head.right!=None:
			self.update(initial_val,final_val,head.right)
		else:
			print("value not in list")



link=LinkedList()
link.insertend(3)
link.insertend(2)
link.insertend(1)
link.insertend(2)

link.postorder()
link.inorder()
val=4
print("Inserting head of {0}".format(val))
link.inserthead(4)
link.postorder()
link.inorder()
val=5
after_val=2
print("Inserting {0} after {1}".format(val,after_val))
link.insertafter(after_val,val)
link.postorder()
link.inorder()
val=6 
before_val=1
print("Inserting {0} before {1}".format(val,before_val))
link.insertbefore(before_val,val)
link.postorder()
link.inorder()

val=1
link.delete(val)
print("After delete of {0}".format(val))
link.postorder()
link.inorder()
val=3
new_val=4
link.update(val,new_val)
print("After update of {0} to {1}".format(val,new_val))
link.postorder()
link.inorder()
