class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []
        
    def is_empty(self):
        return len(self.__stack) == 0
    def is_full(self):
        len (self.__stack) == self.__capacity
        
    def push(self,value):
        if self.is_full():
            print ('Overflow')
        else:
            self.__stack.append(value)    
    def pop(self):
        if self.is_empty():
            print ('UnderFlow')
        else:
            self.__stack.pop()
    
    def top (self):
        if self.is_empty():
            return "Stack is empty"
        return self.__stack[-1]     
my_stack = MyStack(4) 
   
my_stack.push(5)
print (my_stack.top())
my_stack.pop()

print (my_stack.is_empty())
        