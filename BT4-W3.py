class MyQueue:
    def __init__(self, capacity):
         self.__capacity = capacity
         self.__queue = []
        
    def is_empty(self):
        return len(self.__queue) == 0
    def is_full(self):
        len (self.__queue) == self.__capacity
        
    def enqueue(self,value):
        if self.is_full():
            print ('Overflow')
        else:
            self.__queue.append(value)    
    def dequeue(self):
        if self.is_empty():
            print ('UnderFlow')
        else:
            self.__queue.pop(0)
    
    def front (self):
        if self.is_empty():
            return "Queue is empty"
        return self.__queue[0]     
my_queue = MyQueue(5) 
   
my_queue.enqueue (4)
print (my_queue.front())
my_queue.dequeue()

print (my_queue.is_empty())