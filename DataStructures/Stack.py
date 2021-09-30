class Stack:
        def Initialiser(DataItems):
                Stack=[None for i in range(DataItems)]
                return Stack
        def __init__(self,DataItems):
                self.__Stack=Stack.Initialiser(DataItems)
                self.__TopOfStack=0
                self.__temp=0
                self.__BaseOfStack=0
        def push(self,value):
                if self.__Stack[self.__BaseOfStack]==None:
                        self.__Stack[self.__BaseOfStack]=value
                else:
                        self.__TopOfStack+=1
                        if self.__TopOfStack>=len(self.__Stack):
                                print("Stack is Full")
                                self.__TopOfStack-=1
                        else:
                                self.__Stack[self.__TopOfStack]=value    
        def pop(self):
                self.__temp=self.__Stack[self.__TopOfStack]
                self.__TopOfStack-=1
                if self.__TopOfStack<0:
                        self.__TopOfStack+=1
                        print("Stack Is Empty")
                return self.__temp
        def peek(self):
                return self.__Stack[self.__TopOfStack]
        def ViewAll(self):
                return self.__Stack
if __name__ == "__main__":
        s = Stack(90)
        s.push("Potato")
        print(s.peek())
        s.push("Tomato")
        print(s.pop())
        print(s.peek())
