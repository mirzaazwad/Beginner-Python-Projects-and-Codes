#Null Pointer set as None instead of -1 as per book, if using array element with index 0
NULL_POINTER=None
class TreeNode:
    def __init__(self,Data=None):
        self.Data=0
        self.LeftPointer=None
        self.RightPointer=None
RootPointer=0
FreePtr=0
Tree=[0 for i in range(7)]
def InitialiseTree():
    global RootPointer
    global FreePtr
    RootPointer=NULL_POINTER
    FreePtr=1
    for i in range(7):
        Tree[i]=TreeNode()
        Tree[i].LeftPointer=i+1
    Tree[6].LeftPointer=NULL_POINTER
def InsertNode(NewItem):
    global RootPointer
    global FreePtr
    if FreePtr!=NULL_POINTER:#Checks for space in array
        NewNodePtr=FreePtr #take node from free list, store data items and set null pointer
        FreePtr=Tree[FreePtr].LeftPointer
        Tree[NewNodePtr].Data=NewItem
        Tree[NewNodePtr].LeftPointer=NULL_POINTER
        Tree[NewNodePtr].RightPointer=NULL_POINTER
        if RootPointer==NULL_POINTER:
            RootPointer=NewNodePtr
        else:
            ThisNodePtr=RootPointer
            while ThisNodePtr!=NULL_POINTER:
                PreviousNodePtr=ThisNodePtr
                if Tree[ThisNodePtr].Data>NewItem:
                    TurnedLeft=True
                    ThisNodePtr=Tree[ThisNodePtr].LeftPointer
                else:
                    TurnedLeft=False
                    ThisNodePtr=Tree[ThisNodePtr].RightPointer
            if TurnedLeft==True:
                Tree[PreviousNodePtr].LeftPointer=NewNodePtr
            else:
                Tree[PreviousNodePtr].RightPointer=NewNodePtr

def FindNode(SearchItem):
    global RootPointer
    global FreePtr
    ThisNodePtr=RootPointer
    while ThisNodePtr!=NULL_POINTER and Tree[ThisNodePtr].Data!=SearchItem:
        if Tree[ThisNodePtr].Data>SearchItem:
            ThisNodePtr=Tree[ThisNodePtr].LeftPointer #follow left pointer
        else:
            ThisNodePtr=Tree[ThisNodePtr].RightPointer
    return ThisNodePtr
def inorder(r=None):
    global RootPointer
    if r==None:
        r=Tree[RootPointer]
    else:
        r=Tree[r]
    if r.LeftPointer != None:
            inorder(r.LeftPointer)
    print(r.Data)
    if r.RightPointer != None:
            inorder(r.RightPointer)
def preorder(r=None):
    global RootPointer
    if r==None:
        r=Tree[RootPointer]
    else:
        r=Tree[r]
    print(r.Data)
    if r.LeftPointer != None:
            inorder(r.LeftPointer)
    
    if r.RightPointer != None:
            inorder(r.RightPointer)
def postorder(r=None):
    global RootPointer
    if r==None:
        r=Tree[RootPointer]
    else:
        r=Tree[r]
    if r.LeftPointer != None:
            inorder(r.LeftPointer)
    
    if r.RightPointer != None:
            inorder(r.RightPointer)

    print(r.Data)




InitialiseTree()
InsertNode(21)
for i in range(18,24):
	if i!=21:
		InsertNode(i)
inorder()
print("\n \n \n")
preorder()
print("\n \n \n")
postorder()
            
        

        
        
