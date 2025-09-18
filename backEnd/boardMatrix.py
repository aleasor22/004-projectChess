##List of Imports


class MATRIX():
	def __init__(self):
		self.__columnID = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		self.__rowID = ["1", "2", "3", "4", "5", "6", "7", "8"]

		self.__myMatrix = []

		for letter in self.__columnID:
			column = []
			for rowInt in self.__rowID:
				column.append(f"{letter}{rowInt}")
			self.__myMatrix.append(column)
	
	def findMatrixIndex(self, location):
		if self.foundInMatrix(location):
			for i in range(8):
				for j in range(8):
					if self.__myMatrix[i][j] == location:
						return (i, j)

	def foundInMatrix(self, location):
		for i in range(8):
			for j in range(8):
				if self.__myMatrix[j][i] == location:
					return True
		return False
	
	def printMyMatrix(self, easyToRead=True): ##For Debugging Purposes
		if easyToRead:
			print("Easy to read print out - Method Two")
			for i in range(8):
				for j in range(8):
					print(self.__myMatrix[j][i], end=" ")
				print()
		else:
			print(self.__myMatrix)

	def get_matrix(self):
		return self.__myMatrix

	def get_tagAtIndex(self, col, row):
		return self.__myMatrix[col][row]

	##TEMP METHODS
	##TODO REMOVE LATER:
	def get_columnIDs(self):
		return self.__columnID