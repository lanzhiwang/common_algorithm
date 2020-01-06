#!/usr/bin/python


class Heap:
	def __init__(self):
		self.h = []
		self.currsize = 0

	def leftChild(self, i):
		if 2*i+1 < self.currsize:
			return 2*i+1
		return None

	def rightChild(self, i):
		if 2*i+2 < self.currsize:
			return 2*i+2
		return None

	def maxHeapify(self, node):
		if node < self.currsize:
			m = node
			lc = self.leftChild(node)
			rc = self.rightChild(node)
			if lc is not None and self.h[lc] > self.h[m]:
				m = lc
			if rc is not None and self.h[rc] > self.h[m]:
				m = rc
			if m != node:
				self.h[node], self.h[m] = self.h[m], self.h[node]
				self.maxHeapify(m)

	def buildHeap(self, a):
		self.currsize = len(a)
		self.h = list(a)
		if self.currsize <= 1:
			return
		for i in range(self.currsize//2 - 1, -1, -1):
			self.maxHeapify(i)

	def getMax(self):
		if self.currsize >= 1:
			me = self.h[0]
			self.h[0] = self.h.pop(-1)
			self.currsize -= 1
			self.maxHeapify(0)
			return me
		return None

	def heapSort(self):
		size = self.currsize
		for j in range(size - 1, 0, -1):
			self.h[0], self.h[j] = self.h[j], self.h[0]
			self.currsize -= 1
			self.maxHeapify(0)
		self.currsize = size

	def insert(self, data):
		self.h.append(data)
		curr = (self.currsize - 1) // 2
		self.currsize += 1
		while curr >= 0:
			self.maxHeapify(curr)
			curr = (curr - 1) // 2

	def display(self):
		print(self.h)

def main():
	l = [99, 5, 36, 7, 22, 17, 92, 12, 2, 19, 25, 28, 1, 46]
	h = Heap()
	h.buildHeap(l)
	h.display()  # [99, 25, 92, 12, 22, 28, 46, 7, 2, 19, 5, 17, 1, 36]

	print(h.getMax())
	h.display()  # [92, 25, 46, 12, 22, 28, 36, 7, 2, 19, 5, 17, 1]

	h.insert(100)
	h.display()  # [100, 25, 92, 12, 22, 28, 46, 7, 2, 19, 5, 17, 1, 36]

	h.heapSort()
	h.display()  # [1, 2, 5, 7, 12, 17, 19, 22, 25, 28, 36, 46, 92, 100]

if __name__=='__main__':
	main()


