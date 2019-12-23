# Python code to demonstrate working of
# extend(), extendleft(), rotate(), reverse()

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3,])

# using extend() to add numbers to right end
# adds 4,5,6 to right end
de.extend([4,5,6])

# printing modified deque
print("The deque after extending deque at end is : ")
print(de)  # deque([1, 2, 3, 4, 5, 6])

# using extendleft() to add numbers to left end
# adds 7,8,9 to right end
de.extendleft([7,8,9])

# printing modified deque
print("The deque after extending deque at beginning is : ")
print(de)  # deque([9, 8, 7, 1, 2, 3, 4, 5, 6])

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)

# printing modified deque
print("The deque after rotating deque is : ")
print(de)  # deque([1, 2, 3, 4, 5, 6, 9, 8, 7])

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print("The deque after reversing deque is : ")
print(de)  # deque([7, 8, 9, 6, 5, 4, 3, 2, 1])
