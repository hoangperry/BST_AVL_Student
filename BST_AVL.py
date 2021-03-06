import datetime

class Node:
	def __init__(self, key, size:int):
		self.key = key
		self.size = size
		self.left = None
		self.right = None

class Node1:
	def __init__(self, key, size:int, height:int):
		self.key = key
		self.size = size
		self.height = height
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

	def printNode(self, x:Node):
		print(x.key)
		print(x.left.key)
		print(x.right.key)

	def size(self) -> int:
		return self.sizeNode(self.root)

	def sizeNode(self, x:Node) -> int:
		if x == None:
			return 0
		return x.size

	def height(self) -> int:
		return  self.heightNode(self.root)

	def heightNode(self, x:Node) -> int:
		if x == None:
			return -1
		else:
			leftHeight = self.heightNode(x.left)
			rightHeight = self.heightNode(x.right)
			if leftHeight > rightHeight:
				return leftHeight + 1
			return  rightHeight + 1


	def put(self, key):
		self.root = self.putNode(self.root, key)

	def putNode(self, x:Node, key) -> Node:
		if x == None:
			return Node(key, 1)
		if key < x.key:
			x.left = self.putNode(x.left, key)
		elif key > x.key:
			x.right = self.putNode(x.right, key)
		else:
			x.key = key;
		x.size = 1 + self.sizeNode(x.left) + self.sizeNode(x.right);
		return x

	def lrn(self):
		return self.lrnNode(self.root)


	def lrnNode(self, x:Node):
		retStr = ""
		if x != None:
			retStr += self.lrnNode(x.left)
			retStr += self.lrnNode(x.right)
			print(str(x.key) + " ")
			retStr += (str(x.key) + "\n")
		return retStr

	def lnr(self):
		return self.lnrNode(self.root)

	def lnrNode(self, x:Node):
		retStr = ""
		if x != None:
			retStr += self.lnrNode(x.left)
			retStr += (str(x.key) + "\n")
			print(str(x.key) + " ")
			retStr += self.lnrNode(x.right)
		return retStr

	def nlr(self):
		return self.nlrNode(self.root)

	def nlrNode(self, x:Node):
		retStr = ""
		if x != None:
			retStr += (str(x.key) + "\n")
			print(str(x.key) + " ")
			retStr += self.nlrNode(x.left)
			retStr += self.nlrNode(x.right)
		return retStr

	def nlrNoPrint(self):
		return self.nlrNodeNoPrint(self.root)

	def nlrNodeNoPrint(self, x:Node):
		ret = []
		if x != None:
			ret.append(x)
			ret += self.nlrNodeNoPrint(x.left)
			ret += self.nlrNodeNoPrint(x.right)
		return ret

	def nrl(self):
		return self.nrlNode(self.root)

	def nrlNode(self, x:Node):
		retStr = ""
		if x != None:
			retStr += (str(x.key) + "\n")
			print(str(x.key) + " ")
			retStr += self.nrlNode(x.right)
			retStr += self.nrlNode(x.left)
		return retStr
			
	def rnl(self):
		return self.rnlNode(self.root)

	def rnlNode(self, x:Node):
		retStr = ""
		if x != None:
			retStr += self.rnlNode(x.right)
			retStr += (str(x.key) + "\n")
			print(str(x.key) + " ")
			retStr += self.rnlNode(x.left)
		return retStr

	def rln(self):
		return self.rlnNode(self.root)

	def rlnNode(self, x:Node):
		retStr = ""
		if x != None:
			retStr += self.rlnNode(x.right)
			retStr += self.rlnNode(x.left)
			retStr += (str(x.key) + "\n")
			print(str(x.key) + " ")
		return retStr
			
	def get(self, key) -> Node:
		return self.getNode(self.root, key)

	def getNode(self, x:Node, key) -> Node:
		if x == None:
			return x
		if key < x.key:
			return self.getNode(x.left, key)
		elif key > x.key:
			return self.getNode(x.right, key)
		else:
			return x

	def searchWithName(self, key:str):
		self.searchWithNameNode(self.root, key)

	def searchWithNameNode(self, x:Node, key:str):
		if x != None:
			if x.key.name == key:
				print(x.key)
			self.searchWithNameNode(x.right, key)
			self.searchWithNameNode(x.left, key)

	def searchWithID(self, key:int):
		self.searchWithIDNode(self.root, key)

	def searchWithIDNode(self, x:Node, key:int):
		if x != None:
			if x.key.id == key:
				print(x.key)
			self.searchWithIDNode(x.right, key)
			self.searchWithIDNode(x.left, key)
		
	def searchWithBirthday(self, key:str):
		self.searchWithBirthdayNode(self.root, key)

	def searchWithBirthdayNode(self, x:Node, key:str):
		if x != None:
			if x.key.birthday == key:
				print(x.key)
			self.searchWithBirthdayNode(x.right, key)
			self.searchWithBirthdayNode(x.left, key)

	def searchWithCredit(self, key:int):
		self.searchWithCreditNode(self.root, key)

	def searchWithCreditNode(self, x:Node, key:int):
		if x != None:
			if x.key.credit == key:
				print(x.key)
			self.searchWithCreditNode(x.right, key)
			self.searchWithCreditNode(x.left, key)

	def searchWithScore(self, key:float):
		self.searchWithScoreNode(self.root, key)

	def searchWithScoreNode(self, x:Node, key:float):
		if x != None:
			if x.key.score == key:
				print(x.key)
			self.searchWithScoreNode(x.right, key)
			self.searchWithScoreNode(x.left, key)

	def min(self) -> Node:
		return self.minNode(self.root)

	def minNode(self, x:Node) -> Node:
		if x.left == None:
			return x
		return self.minNode(x.left)

	def max(self) -> Node:
		return self.maxNode(self.root)

	def maxNode(self, x:Node) -> Node:
		if x.right == None:
			return x
		return self.maxNode(x.right)

	def findMinMax(self):
		print("Min = " + str(self.minNode(self.root).key))
		print("Max = " + str(self.maxNode(self.root).key))
	
	def createTree(self, inp:list):
		for i in inp:
			self.put(i)

	def creatLeftSkewTree(self, inp:list):
		inp = sorted(inp)
		for i in inp :
			self.put(i)

	def creatRightSkewTree(self, inp:list):
		inp = sorted(inp, reverse=True)
		for i in inp :
			self.put(i)

	def printAsc(self):
		self.lnrNode(self.root)

	def printDsc(self):
		self.rnlNode(self.root)

	def contains(self, key) -> bool:
		return self.getNode(self.root, key) != None

	def containsID(self, id) -> bool:
		return self.getNodeWithID(self.root, id) != None

	def getNodeWithID(self, x:Node, id) -> Node:
		if x != None:
			if id < x.key.id:
				return self.getNodeWithID(x.left, id)
			elif id > x.key.id:
				return self.getNodeWithID(x.right, id)
			return x
		return None

	def deleteMin(self):
		self.root = self.deleteMinNode(self.root)

	def deleteMinNode(self, x:Node)-> Node:
		if x.left == None:
			return x.right
		x.left = self.deleteMinNode(x.left)
		x.size = self.sizeNode(x.left) + self.sizeNode(x.right) + 1
		return x

	def delete(self, key):
		self.root = self.deleteNode(self.root, key)

	def deleteNode(self, x:Node, key) -> Node:
		if x == None:
			return x
		if key < x.key:
			x.left = self.deleteNode(x.left, key)
		elif key > x.key:
			x.right = self.deleteNode(x.right, key)
		else:
			if x.right == None:
				return x.left
			if x.left == None:
				return x.right

			t = x
			x = self.minNode(t.right)
			x.right = self.deleteMinNode(t.right)
			x.left = t.left
		x.size = self.sizeNode(x.left) + self.sizeNode(x.right) + 1
		return x

	def deleteMax(self):
		self.root = self.deleteMaxNode(self.root)

	def deleteMaxNode(self, x:Node) -> Node:
		if x.right == None:
			return x.left
		x.right = self.deleteMaxNode(x.right)
		x.size = self.sizeNode(x.left) + self.sizeNode(x.right) + 1
		return x

	def deleteList(self, inp:list):
		for i in inp:
			self.root = self.deleteNode(self.root, i)

	def getPredecessor(self, key) -> Node:
		if self.get(key) == None:
			return None
		if self.get(key).left != None:
			return self.maxNode(self.get(key).left)
		return None

	def getSuccessor(self, key) -> Node:
		if self.get(key) == None:
			return None
		if self.get(key).right != None:
			return self.minNode(self.get(key).right)
		return None

	def updateName(self, id:int, name:str):
		self.updateNameNode(self.root, id, name)

	def updateNameNode(self, x:Node, id:int, name:str):
		if x != None:
			if id < x.key.id:
				self.updateNameNode(x.left, id, name)
			elif id > x.key.id:
				self.updateNameNode(x.right, id, name)
			else:
				x.key.name = name

	def updateBirthday(self, id:int, birthday:str):
		try:
			datetime.datetime.strptime(birthday, '%d/%m/%Y')
		except ValueError:
			raise ValueError("Incorrect data format, should be DD/MM/YYYY")
		self.updateBirthdayNode(self.root, id, birthday)

	def updateBirthdayNode(self, x:Node, id:int, birthday:str):
		if x != None:
			if id < x.key.id:
				self.updateNameNode(x.left, id, birthday)
			elif id > x.key.id:
				self.updateNameNode(x.right, id, birthday)
			else:
				x.key.birthday = birthday

	def updateCredit(self, id:int, credit:int):
		self.updateCreditNode(self.root, id, credit)

	def updateCreditNode(self, x:Node, id:int, credit:int):
		if x != None:
			if id < x.key.id:
				self.updateCreditNode(x.left, id, credit)
			elif id > x.key.id:
				self.updateCreditNode(x.right, id, credit)
			else:
				x.key.credit = credit

	def updateScore(self, id:int, score:float):
		if score > 10:
			raise ValueError("Credit must less than 10")
		self.updateScoreNode(self.root, id, score)

	def updateScoreNode(self, x:Node, id:int, score:float):
		if x != None:
			if id < x.key.id:
				self.updateScoreNode(x.left, id, score)
			elif id > x.key.id:
				self.updateScoreNode(x.right, id, score)
			else:
				x.key.score = score

###########################
# AVL
###########################

class AVL:
	def __init__(self):
		self.root = None

	def printNode(self, x:Node1):
		print(x.key)
		print(x.left.key)
		print(x.right.key)

	def size(self) -> int:
		return self.sizeNode(self.root)

	def sizeNode(self, x:Node1) -> int:
		if x == None:
			return 0
		return x.size

	def height(self) -> int:
		return self.heightNode(self.root)

	def heightNode(self, x:Node1) -> int:
		if x == None:
			return -1
		return x.height

	def put(self, key):
		self.root = self.putNode(self.root, key)

	def putNode(self, x:Node1, key) -> Node1:
		if x == None:
			return Node1(key, 1, 0)
		if key < x.key:
			x.left = self.putNode(x.left, key)
		elif key > x.key:
			x.right = self.putNode(x.right, key)
		else:
			x.key = key
		x.size = 1 + self.sizeNode(x.left) + self.sizeNode(x.right)
		x.height = 1 + max(self.heightNode(x.left), self.heightNode(x.right))

		return x

	def putBalance(self, key):
		self.root = self.putBalanceNode(self.root, key)

	def putBalanceNode(self, x:Node1, key) -> Node1:
		if x == None:
			return Node1(key, 1, 0)
		if key < x.key:
			x.left = self.putBalanceNode(x.left, key)
		elif key > x.key:
			x.right = self.putBalanceNode(x.right, key)
		else:
			x.key = key
		x.size = 1 + self.sizeNode(x.left) + self.sizeNode(x.right)
		x.height = 1 + max(self.heightNode(x.left), self.heightNode(x.right))

		return self.balanceNode(x)

	def balanceFactor(self, x:Node1) -> int:
		return self.heightNode(x.left) - self.heightNode(x.right)

	def checkBalance(self) -> bool:
		if abs(self.balanceFactor(self.root)) > 1:
			return False
		return True

	def rotateRight(self, x:Node1) -> Node1:
		y = x.left
		x.left = y.right
		y.right = x
		y.size = x.size
		x.size = 1 + self.sizeNode(x.left) + self.sizeNode(x.right)
		x.height = 1 + max(self.heightNode(x.left), self.heightNode(x.right))
		y.height = 1 + max(self.heightNode(y.left), self.heightNode(y.right))
		return y

	def rotateLeft(self, x:Node1) -> Node1:
		y = x.right
		x.right = y.left
		y.left = x
		y.size = x.size
		x.size = 1 + self.sizeNode(x.left) + self.sizeNode(x.right)
		x.height = 1 + max(self.heightNode(x.left), self.heightNode(x.right))
		y.height = 1 + max(self.heightNode(y.left), self.heightNode(y.right))
		return y

	def balance(self):
		while abs(self.balanceFactor(self.root)) > 1:
			self.root = self.balanceNode(self.root)

	def balanceNode(self, x:Node1) -> Node1:
		if self.balanceFactor(x) < -1:
			if self.balanceFactor(x.right) > 0:
				x.right = self.rotateRight(x.right)
			x = self.rotateLeft(x)
		elif self.balanceFactor(x) > 1:
			if self.balanceFactor(x.left) < 0:
				x.left = self.rotateLeft(x.left)
			x = self.rotateRight(x)
		return x

	def lrn(self):
		return self.lrnNode(self.root)

	def lrnNode(self, x: Node):
		retStr = ""
		if x != None:
			retStr += self.lrnNode(x.left)
			retStr += self.lrnNode(x.right)
			print(str(x.key) + " ")
			retStr += (str(x.key) + "\n")
		return retStr

	def lnr(self):
		return self.lnrNode(self.root)

	def lnrNode(self, x: Node):
		retStr = ""
		if x != None:
			retStr += self.lnrNode(x.left)
			retStr += (str(x.key) + "\n")
			print(str(x.key) + " ")
			retStr += self.lnrNode(x.right)
		return retStr

	def nlr(self):
		return self.nlrNode(self.root)

	def nlrNode(self, x: Node):
		retStr = ""
		if x != None:
			retStr += (str(x.key) + "\n")
			print(str(x.key) + " ")
			retStr += self.nlrNode(x.left)
			retStr += self.nlrNode(x.right)
		return retStr

	def nlrNoPrint(self):
		return self.nlrNodeNoPrint(self.root)

	def nlrNodeNoPrint(self, x:Node):
		ret = []
		if x != None:
			ret.append(x)
			ret += self.nlrNodeNoPrint(x.left)
			ret += self.nlrNodeNoPrint(x.right)
		return ret

	def nrl(self):
		return self.nrlNode(self.root)

	def nrlNode(self, x: Node):
		retStr = ""
		if x != None:
			retStr += (str(x.key) + "\n")
			print(str(x.key) + " ")
			retStr += self.nrlNode(x.right)
			retStr += self.nrlNode(x.left)
		return retStr

	def rnl(self):
		return self.rnlNode(self.root)

	def rnlNode(self, x: Node):
		retStr = ""
		if x != None:
			retStr += self.rnlNode(x.right)
			retStr += (str(x.key) + "\n")
			print(str(x.key) + " ")
			retStr += self.rnlNode(x.left)
		return retStr

	def rln(self):
		return self.rlnNode(self.root)

	def rlnNode(self, x: Node):
		retStr = ""
		if x != None:
			retStr += self.rlnNode(x.right)
			retStr += self.rlnNode(x.left)
			retStr += (str(x.key) + "\n")
			print(str(x.key) + " ")
		return retStr



	def getNodeWithID(self, x:Node, id) -> Node:
		if x != None:
			if id < x.key.id:
				return self.getNodeWithID(x.left, id)
			elif id > x.key.id:
				return self.getNodeWithID(x.right, id)
			return x
		return None

	def get(self, key) -> Node1:
		return self.getNode(self.root, key)

	def getNode(self, x:Node1, key) -> Node1:
		if x == None:
			return None
		if key < x.key:
			return self.getNode(x.left, key)
		elif key > x.key:
			return self.getNode(x.right, key)
		else:
			return x

	def contains(self, key) -> bool:
		return self.getNode(self.root, key) != None

	def containsID(self, id) -> bool:
		return self.getNodeWithID(self.root, id) != None

	def min(self) -> Node1:
		return self.minNode(self.root)

	def minNode(self, x:Node1) -> Node1:
		if x.left == None:
			return x
		return self.minNode(x.left)

	def max(self) -> Node1:
		return self.maxNode(self.root)

	def maxNode(self, x:Node1) -> Node1:
		if x.right == None:
			return x
		return self.maxNode(x.right)

	def findMinMax(self):
		print("Min = " + str(self.minNode(self.root).key))
		print("Max = " + str(self.maxNode(self.root).key))

	def deleteMin(self):
		self.root = self.deleteMinNode(self.root)

	def deleteMinNode(self, x:Node1) -> Node1:
		if x.left == None:
			return x.right
		x.left = self.deleteMinNode(x.left)
		x.size = 1 + self.sizeNode(x.left) + self.sizeNode(x.right)
		x.height = 1 + max(self.heightNode(x.left), self.heightNode(x.right))
		return self.balanceNode(x)

	def deleteMax(self):
		self.root = self.deleteMaxNode(self.root)

	def deleteMaxNode(self, x:Node1) -> Node1:
		if x.right == None:
			return x.left
		x.right = self.deleteMaxNode(x.right)
		x.size = 1 + self.sizeNode(x.left) + self.sizeNode(x.right)
		x.height = 1 + max(self.heightNode(x.left), self.heightNode(x.right))
		return self.balanceNode(x)

	def delete(self, key):
		if not self.contains(key):
			return
		self.root = self.deleteNode(self.root, key)

	def deleteNode(self, x:Node1, key) -> Node1:
		if key < x.key:
			x.left = self.deleteNode(x.left, key)
		elif key > x.key:
			x.right = self.deleteNode(x.right, key)
		else:
			if x.left == None:
				return x.right
			elif x.right == None:
				return x.left
			else:
				y = x
				x = self.minNode(y.right)
				x.right = self.deleteMinNode(y.right)
				x.left = y.left
		x.size = 1 + self.sizeNode(x.left) + self.sizeNode(x.right)
		x.height = 1 + max(self.heightNode(x.left), self.heightNode(x.right))
		return  self.balanceNode(x)

	def createTree(self, inp:list):
		for i in inp:
			self.putBalance(i)

	def getPredecessor(self, key) -> Node:
		if self.get(key) == None:
			return None
		if self.get(key).left != None:
			return self.maxNode(self.get(key).left)
		return None

	def getSuccessor(self, key) -> Node:
		if self.get(key) == None:
			return None
		if self.get(key).right != None:
			return self.minNode(self.get(key).right)
		return None


	def updateName(self, id:int, name:str):
		self.updateNameNode(self.root, id, name)

	def updateNameNode(self, x:Node1, id:int, name:str):
		if x != None:
			if id < x.key.id:
				self.updateNameNode(x.left, id, name)
			elif id > x.key.id:
				self.updateNameNode(x.right, id, name)
			else:
				x.key.name = name

	def updateBirthday(self, id:int, birthday:str):
		try:
			datetime.datetime.strptime(birthday, '%d/%m/%Y')
		except ValueError:
			raise ValueError("Incorrect data format, should be DD/MM/YYYY")
		self.updateBirthdayNode(self.root, id, birthday)

	def updateBirthdayNode(self, x:Node1, id:int, birthday:str):
		if x != None:
			if id < x.key.id:
				self.updateNameNode(x.left, id, birthday)
			elif id > x.key.id:
				self.updateNameNode(x.right, id, birthday)
			else:
				x.key.birthday = birthday

	def updateCredit(self, id:int, credit:int):
		self.updateCreditNode(self.root, id, credit)

	def updateCreditNode(self, x:Node1, id:int, credit:int):
		if x != None:
			if id < x.key.id:
				self.updateCreditNode(x.left, id, credit)
			elif id > x.key.id:
				self.updateCreditNode(x.right, id, credit)
			else:
				x.key.credit = credit

	def updateScore(self, id:int, score:float):
		if score > 10:
			raise ValueError("Credit must less than 10")
		self.updateScoreNode(self.root, id, score)

	def updateScoreNode(self, x:Node1, id:int, score:float):
		if x != None:
			if id < x.key.id:
				self.updateScoreNode(x.left, id, score)
			elif id > x.key.id:
				self.updateScoreNode(x.right, id, score)
			else:
				x.key.score = score
