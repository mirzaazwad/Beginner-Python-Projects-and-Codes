class queue:
    @staticmethod
    def initialiser(DataItems):
      Queue=[None for index in range(DataItems)]
      return Queue
    def __init__(self,DataItems = 20):
        self.__head=0
        self.__tail=0
        self.__temp=0
        self.Queue=queue.initialiser(DataItems)
    def add(self,value):
        if self.Queue[self.__tail]==None:
            self.Queue[self.__tail]=value
        else:
            self.__head+=1
            if self.__head>=len(self.Queue):
                print("Queue is Full-Overflow")
                self.__head=0
            else:
                self.Queue[self.__head]=value
    def remove(self):
        self.__temp=self.Queue[self.__tail]
        self.Queue[self.__tail]=None
        if self.__tail<len(self.Queue):
            self.__tail+=1
        else:
            self.__tail=0
        return self.__temp
    def peek(self):
        return self.Queue[self.__tail]
    
        
        
        
if __name__ == "__main__":
    q = queue()
    q.add("Tomato")
    q.add("Potato")
    q.add("Watermelon")

    print(q.peek())
    print(q.remove())
    print(q.peek())
    print(q.remove())
    
