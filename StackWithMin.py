# This is an implementation of a Stack class that also keeps track of the minimum element in the stack. 
# The idea is to keep track while trying to minimize Space Complexity in addition to Time Complexity
# What we will notice is that we can try and implement the Stack with Time Complexity Optimized to ~ O(1)
# However, in the case that the elements inserted into the Stack are in reversesorted order, we have Space Complexity = O(n)
# Therefore, in the Armortized Analysis, we have Time Complexity = O(1), and Space Complexity : O(alpha), alpha ~ 1
# However, in the Worst-Case Analysis, we have Time Complexity = O(1), and Space Compleixty : O(n)

import Queue

class StackWithMin:

  def __init__(self):
    self.minStack = None
    self.stack = None
    self.length = 0
    self.lengthMinStack = 0
  
  def __init__(self, firstInt):
    self.minStack = [firstInt]
    self.stack = [firstInt]
    self.length = 1
    self.lengthMinStack = 1
    
  def push(self, newInt):
    if self.length == 0:
      self.minStack = [newInt]
      self.stack = [newInt]
      self.length = 1
      self.lengthMinStack = 1
    else:
      if newInt < self.minStack[self.lengthMinStack - 1]:
        self.minStack.append(newInt)
        self.lengthMinStack += 1
      self.stack.append(newInt)
      self.length += 1
  
  def pop():
    if self.stack[self.length - 1] == self.minStack[self.lengthMinStack - 1]:
      self.stack.pop()
      self.length -= 1
      currMin = self.minStack.pop()
      self.lengthMinStack -= 1
      return currMin
    else:
      currElem = self.stack.pop()
      self.length -= 1
      retun currElem
  
  def getMin():
    if self.lengthMinStack == 0:
      return None
    else:
      return self.minStack[self.lengthMinStack - 1]

      
      
