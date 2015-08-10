# In this file we will implement a Queue using 2 Stacks.
# While we previously implemented a Stack with a getMin() operation in constant time, in this question we will assume:
# 1) An implemented stack Class
# We will try to optimize the typical queue operations:
# 1) push()
# 2) pop()

import queue

class QueueWithTwoStacks:
  def __init__(self):
    self.stackOne = queue.LifoQueue()
    self.stackTwo = queue.LifoQueue()
  
  def push(self, currValue):
    self.stackOne.put(currValue)
    
  def reverseOrder(self):
    while not self.stackOne.empty():
      currElem = self.stackOne.get()
      self.stackTwo.put(currElem)
  
  def pop(self):
    if self.stackTwo.qsize() != 0:
      return self.stackTwo.get()
    elif self.stackOne.qsize() != 0 and self.stackTwo.qsize() == 0:
      reverseOrder(self)
      return self.stackTwo.get()
    else:
      return None
      
