"""
栈 - 先进后出
"""

class Stack:

   def __init__(self):
      self.stack = []
      self.top = 0

   def is_empty(self):
      return self.top == 0

   def push(self, item):
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]

   def __str__(self):
      return 'stack: %s, top: %s' % (self.stack, self.top)


if __name__ == '__main__':
   s = Stack()
   print(s)  # stack: [], top: 0

   s.push(1)
   s.push(2)
   s.push(3)
   s.push(4)
   print(s)  # stack: [1, 2, 3, 4], top: 4

   print(s.pop())  # 4
   print(s)  # stack: [1, 2, 3, 4], top: 3

   s.push(5)
   print(s)  # stack: [1, 2, 3, 5], top: 4
