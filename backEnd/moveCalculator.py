from .advancedMoveLogic import LOGIC

class MOVECALC(LOGIC):
	def __init__(self, chess, ): ##place):
		##Class Variables (w/ Instance Tracking)
		LOGIC.__init__(self, chess)


	def findMyNextMoves(self, object, calcKing=True):
		if "PAWN" in object.myID:
			self.pawnMoveCalc(object.locationID, object)
		elif "ROOK" in object.myID:
			self.rookMoveCalc(object.locationID, object)
		elif "KNIGHT" in object.myID:
			self.knightMoveCalc(object.locationID, object)
		elif "BISHOP" in object.myID:
			self.bishopMoveCalc(object.locationID, object)
		elif "QUEEN" in object.myID:
			self.queenMoveCalc(object.locationID, object)
			# print(f"{object.myID} can  move: {object.moveSet}")
		elif "KING" in object.myID and calcKing:
			self.kingMoveCalc(object.locationID, object)
	
	
	def knightMoveCalc(self, origin, object):
		##Resets
		object.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)

		for i in range(-2, 3):
			for j in range(-2, 3):
				try:
					myGlobLoc = self._myGlobalMatrix[index_A+j][index_B+i]
					if index_A+j < 0 or index_B+i < 0:
						continue
					elif j % 2 == 0 and (i == -2 or i == 2):
						continue
					elif (i==-1 or i==1) and (j>=-1 and j<=1):
						continue
					elif (i==0 and j!=0):
						continue
					self.specialMoves(myGlobLoc, object)
				except IndexError as e:
					# print(e)
					pass
	
	def pawnMoveCalc(self, origin, object):
		##New Call Resets
		object.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)
		try:
			if "-W" in object.myID:
				for location in self.pawnAttackCalc(object.locationID, object):
					if self._chess.MATRIX.foundInPieceMatrix(location):
						self.specialMoves(location, object)
				if self._myPieceMatrix[index_A][index_B+1] == "**":  ##Handdles basic move logic
					if origin[1] == "2" and self._myPieceMatrix[index_A][index_B+2] == "**":
						self.specialMoves(self._myGlobalMatrix[index_A][index_B+2], object)
					self.specialMoves(self._myGlobalMatrix[index_A][index_B+1], object)

			elif "-B" in object.myID:
				for location in self.pawnAttackCalc(object.locationID, object):
					if self._chess.MATRIX.foundInPieceMatrix(location):
						self.specialMoves(location, object)
				if self._myPieceMatrix[index_A][index_B-1] == "**":  ##Handdles basic move logic
					if origin[1] == "7" and self._myPieceMatrix[index_A][index_B-2] == "**":
						self.specialMoves(self._myGlobalMatrix[index_A][index_B-2], object)
					self.specialMoves(self._myGlobalMatrix[index_A][index_B-1], object)
		except IndexError as e:
			# print(f"ERROR @CALC.moveCalculator(): {e}")
			pass

	def bishopMoveCalc(self, origin, object):
		##Resets List
		if "QUEEN" not in object.myID:
			object.moveSet = set()
		
		# list = ["North West", "North East", "South East", "South West"]
		# for direction in list:
		# 	self.directionLooping(origin, object, direction, "red")

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)

		for southEast in range(8):
			try:
				myLoc = self._myPieceMatrix[index_A+southEast][index_B-southEast]
				myGlobLoc = self._myGlobalMatrix[index_A+southEast][index_B-southEast]
				##Logic Here
				if index_A+southEast < 0 or index_B-southEast < 0:
					break
				if myGlobLoc == object.locationID:
					continue
				self.specialMoves(myGlobLoc, object)
				if myLoc != "**":
					break
			except IndexError as e:
				# print(e)
				break

		for southWest in range(8):
			try:
				myLoc = self._myPieceMatrix[index_A-southWest][index_B-southWest]
				myGlobLoc = self._myGlobalMatrix[index_A-southWest][index_B-southWest]
				##Logic Here
				if index_A-southWest < 0 or index_B-southWest < 0:
					break
				if myGlobLoc == object.locationID:
					continue
				self.specialMoves(myGlobLoc, object)
				if myLoc != "**":
					break
			except IndexError as e:
				# print(e)
				break

		for northEast in range(8):
			try:
				myLoc = self._myPieceMatrix[index_A+northEast][index_B+northEast]
				myGlobLoc = self._myGlobalMatrix[index_A+northEast][index_B+northEast]
				##Logic Here
				if index_A+northEast < 0 or index_B+northEast < 0:
					break
				if myGlobLoc == object.locationID:
					continue
				self.specialMoves(myGlobLoc, object)
				if myLoc != "**":
					break
			except IndexError as e:
				# print(e)
				break

		for northWest in range(8):
			try:
				myLoc = self._myPieceMatrix[index_A-northWest][index_B+northWest]
				myGlobLoc = self._myGlobalMatrix[index_A-northWest][index_B+northWest]
				##Logic Here
				if index_A-northWest < 0 or index_B+northWest < 0:
					break
				if myGlobLoc == object.locationID:
					continue
				self.specialMoves(myGlobLoc, object)
				if myLoc != "**":
					break
			except IndexError as e:
				# print(e)
				break
	
	def rookMoveCalc(self, origin, object):
		##Reset
		if "QUEEN" not in object.myID:
			object.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)
		
		## Horizontal Movement
		for east in range(index_A-1, -1, -1):
			myLoc = self._myPieceMatrix[east][index_B]
			myGlobLoc = self._myGlobalMatrix[east][index_B]
			self.specialMoves(myGlobLoc, object)
			if myLoc != "**":
				break

		for west in range(index_A+1, 8):
			myLoc = self._myPieceMatrix[west][index_B] 
			myGlobLoc = self._myGlobalMatrix[west][index_B]
			self.specialMoves(myGlobLoc, object)
			if myLoc != "**":
				break

		# Vertical Movment
		for south in range(index_B-1, -1, -1):
			myLoc = self._myPieceMatrix[index_A][south]
			myGlobLoc = self._myGlobalMatrix[index_A][south]
			self.specialMoves(myGlobLoc, object)
			if myLoc != "**":
				break
		
		for north in range(index_B+1, 8):
			myLoc = self._myPieceMatrix[index_A][north]
			myGlobLoc = self._myGlobalMatrix[index_A][north]
			self.specialMoves(myGlobLoc, object)
			if myLoc != "**":
				break
	
	def queenMoveCalc(self, origin, object):
		object.moveSet = set()
		self.bishopMoveCalc(origin, object)
		self.rookMoveCalc(origin, object)

	def kingMoveCalc(self, origin, object, notCheckmateLogic=True):
		##Rests
		if notCheckmateLogic:
			self.attackingTheKing(object.myID)
		self.potentialThreatsOnKing(object)
		object.moveSet = set()
		
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)
		
		## Castle Logic - The Setup
		if "-W" in object.myID and object.hasMoved == False and object.inCheck == False:
			if self._chess.MATRIX.foundInPieceMatrix("f1") == False and self._chess.MATRIX.foundInPieceMatrix("g1") == False:
				print("White King Sided Castle")
				object.moveSet.add("g1")
			elif self._chess.MATRIX.foundInPieceMatrix("b1") == False and self._chess.MATRIX.foundInPieceMatrix("c1") == False and self._chess.MATRIX.foundInPieceMatrix("d1") == False:
				print("White Queen Sided Castle")
				object.moveSet.add("c1")

		if "-B" in object.myID and object.hasMoved == False and object.inCheck == False:
			if self._chess.MATRIX.foundInPieceMatrix("f8") == False and self._chess.MATRIX.foundInPieceMatrix("g8") == False:
				print("Black King Sided Castle")
				object.moveSet.add("g8")
			elif self._chess.MATRIX.foundInPieceMatrix("b8") == False and self._chess.MATRIX.foundInPieceMatrix("c8") == False and self._chess.MATRIX.foundInPieceMatrix("d8") == False:
				print("Black Queen Sided Castle")
				object.moveSet.add("c8")

		for i in range(-1, 2):
			for j in range(-1, 2):
				try:
					myloc = self._myPieceMatrix[index_A+i][index_B+j]
					myGlobLoc = self._myGlobalMatrix[index_A+i][index_B+j]
					if (index_A+i) < 0 or (index_B+j) < 0:
						raise IndexError
					if myGlobLoc not in object.threats:
						self.specialMoves(myGlobLoc, object)
				except IndexError as e:
					# print(f"Error: {e} \n\t@CALC.kingMoveCalc()")
					continue
		
	def kingCastle(self, location):
		# print(self.get_piece("h1").myID, "this rook king@g1")
		##White King
		if location == "g1" and self.get_pieceAtLocation("h1").hasMoved == False:
			rook = self.get_pieceAtLocation("h1")
			self._chess.get_canvas().delete(rook.canvasID)
			rook.placeImage("f1")
		elif location == "c1" and self.get_pieceAtLocation("a1").hasMoved == False:
			rook = self.get_pieceAtLocation("a1")
			self._chess.get_canvas().delete(rook.canvasID)
			rook.placeImage("d1")
		
		##Black King
		if location == "g8" and self.get_pieceAtLocation("h8").hasMoved == False:
			rook = self.get_pieceAtLocation("h8")
			self._chess.get_canvas().delete(rook.canvasID)
			rook.placeImage("f8")
		elif location == "c8" and self.get_pieceAtLocation("a8").hasMoved == False:
			rook = self.get_pieceAtLocation("a8")
			self._chess.get_canvas().delete(rook.canvasID)
			rook.placeImage("d8")
