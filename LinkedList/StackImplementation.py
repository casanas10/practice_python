# -*- coding: utf-8 -*-
"""
Problem:
Discuss the stack datastructure. Implement a stack in Python
"""

class Node:
	def __init__(self, x):
		self.val = x
		self.next = None

class Stack:
	def __init__(self):
		self.head = None
		self.count = 0

	def push(self, x):
		if self.head is None:
			self.head = Node(x)
			self.count += 1
		else:
			newNode = Node(x)
			self.head = newNode
			newNode.next = None
			self.count += 1

	def pop(self):
		if self.head is None:
			return None
		else:
			popped =self.head.val
			self.head = self.head.next
			self.count -= 1
			return popped
	
	def length(self):
		return self.count
	

def main():
	stack = Stack()
	stack.push(5)
	stack.push(7)
	print(stack.length())
	print(stack.pop())
	print(stack.length())


if __name__ == "__main__":
	main()