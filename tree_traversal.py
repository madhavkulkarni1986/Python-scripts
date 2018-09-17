class Node:
'''
	Class Node to define the node of a tree. A node has a value(int), a left child and a right child.
'''
	def __init__(self, value, left=None, right=None):
		self.value=value
		self.left=left
		self.right=right

def inOrder(root):
'''
In-Order traversal - Left, Root, Right
'''
	if(root is None):
		print("Empty Tree")
		return

	if(root.left):
		inOrder(root.left)
	print(str(root.value),', ',end='')
	if(root.right):
		inOrder(root.right)
def preOrder(root):
'''
Pre-Order traversal - Root, Left, Right
'''	
	if(root is None):
		print("Empty Tree")
		return
	print(str(root.value),', ', end='')
	if(root.left):
		preOrder(root.left)
	if(root.right):
		preOrder(root.right)

def postOrder(root):
'''
Post-Order traversal - Left, Right, Root
'''
	if(root is None):
		print("Empty Tree")
		return

	if(root.left):
		postOrder(root.left)
	if(root.right):
		postOrder(root.right)
	print(str(root.value),', ',end='')

def breadthFirst(root):
'''
Breadth first traversal or Level Order traversal
'''
	if(root is None):
		print("Empty Tree")
		return

	nodeQ=list()
	nodeQ.append(root)

	while(len(nodeQ) > 0):
		print(nodeQ[0].value,', ',end='')
		node=nodeQ.pop(0)
		if(node.left is not None):
			nodeQ.append(node.left)
		if(node.right is not None):
			nodeQ.append(node.right)

## Construct Tree
##          2
##		  /   \
##	     3     4
##      / \   / \
##     6   9 8  12
##    / \
##   12 18

node_left_left1=Node(6,Node(12),Node(18))
node_left1=Node(3,node_left_left1,Node(9))
node_right1=Node(4,Node(8),Node(12))
tree1=Node(2,node_left1,node_right1)

### Start Traversal
print("In-order traversal\nExpected : 12 , 6 , 18 , 3 , 9 , 2 , 8 , 4 , 12 ,")
print("Got      : ",end='')
inOrder(tree1)

print("\n\nPre-Order traversal\nExpected : 2 , 3 , 6 , 12 , 18 , 9 , 4 , 8 , 12 ,")
print("Got      : ",end='')
preOrder(tree1)

print("\n\nPost-Order traversal\nExpected : 12 , 18 , 6 , 9 , 3 , 8 , 12 , 4 , 2 ,")
print("Got      : ",end='')
postOrder(tree1)

print("\n\nBreadth first traversal\nExpected : 2 , 3 , 4 , 6 , 9 , 8 , 12 , 12 , 18 ,")
print("Got      : ",end='')
breadthFirst(tree1)