

class MOVECALC():
	def __init__(self, chess, ): ##place):
		##Class Variables (w/ Instance Tracking)
		self.__chess = chess
		self.__render = chess.get_canvas()
		self.__myGlobalMatrix = chess.MATRIX.get_matrix("Global")
		self.__myPieceMatrix = chess.MATRIX.get_matrix("Piece")
		self.__activeLocaiton = {}
		# self.__place = place ##NOTE: Is this Needed?
	
	def updateActiveLocaitons(self, location, object):
		for key, value in self.__activeLocaiton.items():
			if object == value:
				print(object.myID, "is getting removed")
				del self.__activeLocaiton[key]
				break

		self.__activeLocaiton[location] = object
		# print(f"{object.myID} added to activeLocation[{location}]")

	def bishopMoveCalc(self, location, object):
		##Resets List
		if "QUEEN" not in object.myID:
			object.moveSet = set()

		##Local Variables
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(location)
		for northEast in range(8):
			try:
				if index_B-northEast < 0:
					raise IndexError(f"Index Less than 0 - {index_B-northEast}")
				if northEast == 0:
					object.moveSet.add(self.__myGlobalMatrix[index_A+northEast][index_B-northEast])
				elif self.__myPieceMatrix[index_A+northEast][index_B-northEast] != "**":
					object.moveSet.add(self.__myGlobalMatrix[index_A+northEast][index_B-northEast])
					raise IndexError
				else:
					object.moveSet.add(self.__myGlobalMatrix[index_A+northEast][index_B-northEast])
			except IndexError as e:
				# print(e)
				break
		for northWest in range(8):
			try:
				if index_A-northWest < 0 or index_B-northWest < 0:
					raise IndexError("Index Less than 0")
				if northWest == 0:
					object.moveSet.add(self.__myGlobalMatrix[index_A-northWest][index_B-northWest])
				elif self.__myPieceMatrix[index_A-northWest][index_B-northWest] != "**":
					object.moveSet.add(self.__myGlobalMatrix[index_A-northWest][index_B-northWest])
					raise IndexError
				object.moveSet.add(self.__myGlobalMatrix[index_A-northWest][index_B-northWest])
			except IndexError as e:
				# print(e)
				break
		for southEast in range(8):
			try:
				if southEast == 0:
					object.moveSet.add(self.__myGlobalMatrix[index_A+southEast][index_B+southEast])
				elif self.__myPieceMatrix[index_A+southEast][index_B+southEast] != "**":
					object.moveSet.add(self.__myGlobalMatrix[index_A+southEast][index_B+southEast])
					raise IndexError
				object.moveSet.add(self.__myGlobalMatrix[index_A+southEast][index_B+southEast])
			except IndexError as e:
				# print(e)
				break
		for southWest in range(8):
			try:
				if index_A-southWest < 0:
					raise IndexError("Index Less than 0")
				if southWest == 0:
					object.moveSet.add(self.__myGlobalMatrix[index_A-southWest][index_B+southWest])
				elif self.__myPieceMatrix[index_A-southWest][index_B+southWest] != "**":
					object.moveSet.add(self.__myGlobalMatrix[index_A-southWest][index_B+southWest])
					raise IndexError
				object.moveSet.add(self.__myGlobalMatrix[index_A-southWest][index_B+southWest])
			except IndexError as e:
				# print(e)
				break	
	
	def knightMoveCalc(self, location, object):
		##Resets
		object.moveSet = set()

		##Local Variables
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(location)

		for i in range(-2, 3):
			for j in range(-2, 3):
				try:
					if index_A+j < 0 or index_B+i < 0:
						raise IndexError
					if j % 2 == 0 and (i == -2 or i == 2):
						raise IndexError
					elif (i==-1 or i==1) and (j>=-1 and j<=1):
						raise IndexError
					elif (i==0 and j!=0):
						raise IndexError
					else:
						object.moveSet.add(self.__myGlobalMatrix[index_A+j][index_B+i])
				except IndexError:
					continue
	
	def rookMoveCalc(self, location, object):
		##Reset
		if "QUEEN" not in object.myID:
			object.moveSet = set()

		##Local Variables
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(location)
		
		## Horizontal Movement
		for west in range(index_A-1, -1, -1):
			if self.__myPieceMatrix[west][index_B] != "**":
				object.moveSet.add(self.__myGlobalMatrix[west][index_B])
				break
			object.moveSet.add(self.__myGlobalMatrix[west][index_B])

		for east in range(index_A+1, 8):
			if self.__myPieceMatrix[east][index_B] != "**":
				object.moveSet.add(self.__myGlobalMatrix[east][index_B])
				break
			object.moveSet.add(self.__myGlobalMatrix[east][index_B])

		## Vertical Movment
		for north in range(index_B-1, -1, -1):
			if self.__myPieceMatrix[index_A][north] != "**":
				object.moveSet.add(self.__myGlobalMatrix[index_A][north])
				break
			object.moveSet.add(self.__myGlobalMatrix[index_A][north])
		
		for south in range(index_B+1, 8):
			if self.__myPieceMatrix[index_A][south] != "**":
				object.moveSet.add(self.__myGlobalMatrix[index_A][south])
				break
			object.moveSet.add(self.__myGlobalMatrix[index_A][south])
	
	def queenMoveCalc(self, location, object):
		self.bishopMoveCalc(location, object)
		self.rookMoveCalc(location, object)

	def kingMoveCalc(self, location, object):
		##Rests
		object.moveSet = set()
		
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(location)
		for i in range(-1, 2):
			for j in range(-1, 2):
				try:
					if (index_A+i) < 0 or (index_B+j) < 0:
						raise IndexError("Less than 0")
					if self.__myPieceMatrix[index_A+i][index_B+j] != "**":
						object.moveSet.add(self.__myGlobalMatrix[index_A+i][index_B+j])
						raise IndexError("Spot Used")
					object.moveSet.add(self.__myGlobalMatrix[index_A+i][index_B+j])
				except IndexError as e:
					# print(e)
					continue
	
	def pawnMoveCalc(self, location, object):
		##New Call Resets
		currRow = location[1]
		object.moveSet = set()

		##Local Variables
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(location)

		if "-W" in object.myID:
			try: #Handles General Pawn Movement
				if self.__myPieceMatrix[index_A][index_B+1] == "**":
					object.moveSet.add(self.__myGlobalMatrix[index_A][index_B+1])
				if currRow == "2" and self.__myPieceMatrix[index_A][index_B+2] == "**":
					object.moveSet.add(self.__myGlobalMatrix[index_A][index_B+2])
			except IndexError:
				pass
			try: ##Handles Pawn Attacks
				if self.__myPieceMatrix[index_A-1][index_B+1] != "**":
					object.moveSet.add(self.__myGlobalMatrix[index_A-1][index_B+1])
				if self.__myPieceMatrix[index_A+1][index_B+1] != "**":
					object.moveSet.add(self.__myGlobalMatrix[index_A+1][index_B+1])
			except IndexError:
				pass
		if "-B" in object.myID:
			try: #Handles General Pawn Movement
				if self.__myPieceMatrix[index_A][index_B-1] == "**":
					object.moveSet.add(self.__myGlobalMatrix[index_A][index_B-1])
					if currRow == "7" and self.__myPieceMatrix[index_A][index_B-2] == "**":
						object.moveSet.add(self.__myGlobalMatrix[index_A][index_B-2])
			except IndexError:
				pass
			try: ##Handles Pawn Attacks
				if self.__myPieceMatrix[index_A-1][index_B-1] != "**":
					object.moveSet.add(self.__myGlobalMatrix[index_A-1][index_B-1])
				if self.__myPieceMatrix[index_A+1][index_B-1] != "**":
					object.moveSet.add(self.__myGlobalMatrix[index_A+1][index_B-1])
			except IndexError:
				pass
	
	


