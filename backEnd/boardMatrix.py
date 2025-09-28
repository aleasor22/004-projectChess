##List of Imports


class MATRIX():
	def __init__(self):
		self.__columnID = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		self.__rowID = ["1", "2", "3", "4", "5", "6", "7", "8"]

		self.__myGlobalMatrix = []
		self.__myPieceMatrix = []

		##Global Matrix
		for letter in self.__columnID:
			column = []
			for rowInt in self.__rowID:
				column.append(f"{letter}{rowInt}")
			self.__myGlobalMatrix.append(column)

		
		##Piece Matrix
		for letter in self.__columnID:
			column = []
			for i in range(len(self.__rowID)):
				if i >= 2 and i <= 5:
					column.append("**")
				else:
					column.append(f"{letter}{self.__rowID[i]}")
			self.__myPieceMatrix.append(column)

	def updatePieceMatrix(self, oldLocation, newLocaiton):
		##Not checking for proper locations - may cause issues later
		try:
			# print(f"oldLoc:{oldLocation}\nnewLoc:{newLocaiton}")
			oldIndex_A, oldIndex_B = self.findMatrixIndex(oldLocation)
			newIndex_A, newIndex_B = self.findMatrixIndex(newLocaiton)

			self.__myPieceMatrix[oldIndex_A][oldIndex_B] = "**"
			self.__myPieceMatrix[newIndex_A][newIndex_B] = newLocaiton

			self.printMyPieceMatrix()
			print("Printing @MATRIX.updatePieceMatrix")


		except Exception:
			print("Something messed up: \n\t @MATRIX.updatePieceMatrix")


	def findMatrixIndex(self, location):
		if self.foundInMatrix(location):
			for i in range(8):
				for j in range(8):
					if self.__myGlobalMatrix[i][j] == location:
						return (i, j)

	def foundInMatrix(self, location):
		for i in range(8):
			for j in range(8):
				if self.__myGlobalMatrix[j][i] == location:
					return True
		return False

	def foundInPieceMatrix(self, location):
		for i in range(8):
			for j in range(8):
				if self.__myPieceMatrix[j][i] == location:
					return True
		return False
	
	def printMyGlobalMatrix(self, easyToRead=True): ##For Debugging Purposes
		if easyToRead:
			print("Easy to read print out:")
			for i in range(8):
				for j in range(8):
					print(self.__myGlobalMatrix[j][i], end=" ")
				print()
		else:
			print(self.__myGlobalMatrix)
	
	
	def printMyPieceMatrix(self, easyToRead=True): ##For Debugging Purposes
		if easyToRead:
			print("Easy to read print out:")
			for i in range(8):
				for j in range(8):
					print(self.__myPieceMatrix[j][i], end=" ")
				print()
		else:
			print(self.__myPieceMatrix)

	def get_matrix(self, matrix):
		if matrix == "Piece":
			return self.__myPieceMatrix
		elif matrix == "Global":
			return self.__myGlobalMatrix
		

	def get_tagAtIndex(self, col, row, matrix="Global"):
		if matrix == "Piece":
			return self.__myPieceMatrix[col][row]
		elif matrix == "Global":
			return self.__myGlobalMatrix[col][row]

	##TEMP METHODS
	##TODO REMOVE LATER:
	def get_columnIDs(self):
		return self.__columnID
	
	def get_rowIDs(self):
		return self.__rowID