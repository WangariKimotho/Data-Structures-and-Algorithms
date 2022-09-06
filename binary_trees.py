class BinaryTreeNode:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def add_child(self,data):
		if data ==self.data:
			return
		if data < self.data:
			if self.left:
				self.left.add_child(data)
			else:
				self.left = BinaryTreeNode(data)

		if data > self.data:
			if self.right:
				self.right.add_child(data)
			else:
				self.right = BinaryTreeNode(data)

	def in_order_traversal(self):
		elements = []

		# start with left subtree
		if self.left:
			elements += self.left.in_order_traversal()

		# then base node
		elements.append(self.data)

		# then right subtree
		if self.right:
			elements +=self.right.in_order_traversal()
		return elements	
	def pre_order_traversal(self):
		elements = []

		# root node first
		elements.append(self.data)	

		# left subtree next
		if self.left:
			elements += self.left.pre_order_traversal()

		# right subtree last 
		if self.right:
			elements += self.right.pre_order_traversal()	
		return elements	

	def post_order_traversal(self):
		elements = []

		# left subtree first
		if self.left:
			elements +=self.left.post_order_traversal()

		# right subtree next
		if self.right:
			elements += self.right.post_order_traversal()

		# finally the root node
		elements.append(self.data)

		return elements			

	def search(self,val):
		if val == self.data:
			return True

		if val < self.data:
			if self.left:
				return self.left.search(val)
			else:
				return False
		if val > self.data:
			if self.right:
				return self.right.search(val)
			else:
				return False

	def find_min(self):
		if self.left is None:
			return self.data
		else:
			while self.left:
				if self.left.left is None:
					return self.left.data
				else:	
					self.left = self.left.left
				

	def find_max(self):
		if self.right is None:
			return self.data
			
		return self.right.find_max()	

	def calculate_sum(self):
		# return sum(self.in_order_traversal()) - this one includes duplicate so not cool,
		# also doesn't utilise recursion
		left_sum = 0
		right_sum = 0

		if self.left:
			left_sum += self.left.calculate_sum()
		else:
			0
		if self.right:
			right_sum += self.right.calculate_sum()
		else:
			0
		

		# left_sum = self.left.calculate_sum() if self.left else 0
		# right_sum = self.right.calculate_sum() if self.right else 0
		return self.data + left_sum +right_sum		

	def delete(self,val):
		if val < self.data:
			if self.left:
				self.left = self.left.delete(val)
		elif val > self.data:
			if self.right:
				self.right = self.right.delete(val)
		else:
			if self.left is None and self.right is None:
				return None
			if self.left is None:
				return self.right 
			if self.right is None:
				return self.left  	 

			# min_val = self.right.find_min()
			# self.data = min_val
			# self.right = self.right.delete(min_val)
			max_val = self.left.find_max()
			self.data = max_val
			self.left = self.left.delete(max_val)

		return self				
					

	

def build_tree(elements):
	root = BinaryTreeNode(elements[0])

	for i in range(1,len(elements)):
		root.add_child(elements[i])


	return root

if __name__ =="__main__":
	nums = [12,15,2,23,3,9,5,16,4]
	numbers_tree = build_tree(nums)

	print(numbers_tree.in_order_traversal())
	print(numbers_tree.delete(23 ))
	print(numbers_tree.in_order_traversal())

									
		