

class MOVECALC():
	def __init__(self, chess, ): ##place):
		##Class Variables (w/ Instance Tracking)
		self.__chess = chess
		self.__myGlobalMatrix = chess.MATRIX.get_matrix("Global")
		self.__myPieceMatrix = chess.MATRIX.get_matrix("Piece")
		self.__activeLocaiton = {} ##Key == LocationID, value == PIECE.object @ Location
		# self.__forceTheseMoves = set()

		##Check/Checkmate Logic
		self.WKingCheck = False
		self.BKingCheck = False
	
	

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
		elif "KING" in object.myID and calcKing == True:
			self.kingMoveCalc(object.locationID, object)
	
	def updateActiveLocaitons(self, location, object):
		for key, value in self.__activeLocaiton.items():
			if object == value:
				# print(f"{object.myID} is getting moved to {object.locationID} ")
				del self.__activeLocaiton[key]
				break

		self.__activeLocaiton[location] = object
		# print(f"{object.myID} added to activeLocation[{location}]")

	def captureAble(self, location, object=None):
		"""If the neiboring location is used by an opponent's piece, add it to possible moves"""
		# print(object.myID[-2], " vs ", self.__activeLocaiton[location].myID[-2])
		if object.myID[-2] not in self.__activeLocaiton[location].myID[-2]:
			object.moveSet.add(location)

	def bishopMoveCalc(self, origin, object):
		##Resets List
		if "QUEEN" not in object.myID:
			object.moveSet = set()

		##Local Variables
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(origin)
		for northEast in range(8):
			try:
				myLoc = self.__myPieceMatrix[index_A+northEast][index_B-northEast]
				if index_B-northEast < 0:
					raise IndexError(f"Index Less than 0")
				elif myLoc == object.locationID:
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					raise IndexError
					# if "KING" in self.__activeLocaiton[myLoc].myID:
					# 	continue
					# else:
					# 	raise IndexError
				else:
					object.moveSet.add(self.__myGlobalMatrix[index_A+northEast][index_B-northEast])
			except IndexError as e:
				# print(e)
				break
		for northWest in range(8):
			try:
				myLoc = self.__myPieceMatrix[index_A-northWest][index_B-northWest]
				if index_A-northWest < 0 or index_B-northWest < 0:
					raise IndexError("Index Less than 0")
				elif myLoc == object.locationID:
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					raise IndexError
					# if "KING" in self.__activeLocaiton[myLoc].myID:
					# 	continue
					# else:
					# 	raise IndexError
				else:
					object.moveSet.add(self.__myGlobalMatrix[index_A-northWest][index_B-northWest])
			except IndexError as e:
				# print(e)
				break
		for southEast in range(8):
			try:
				myLoc = self.__myPieceMatrix[index_A+southEast][index_B+southEast]
				if myLoc == object.locationID:
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					raise IndexError
					# if "KING" in self.__activeLocaiton[myLoc].myID:
					# 	continue
					# else:
					# 	raise IndexError
				else:
					object.moveSet.add(self.__myGlobalMatrix[index_A+southEast][index_B+southEast])
			except IndexError as e:
				# print(e)
				break
		for southWest in range(8):
			try:
				myLoc = self.__myPieceMatrix[index_A-southWest][index_B+southWest]
				if index_A-southWest < 0:
					raise IndexError("Index Less than 0")
				elif myLoc == object.locationID:
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					raise IndexError
					# if "KING" in self.__activeLocaiton[myLoc].myID:
					# 	continue
					# else:
					# 	raise IndexError
				else:
					object.moveSet.add(self.__myGlobalMatrix[index_A-southWest][index_B+southWest])
			except IndexError as e:
				# print(e)
				break	
	
	def knightMoveCalc(self, origin, object):
		##Resets
		object.moveSet = set()

		##Local Variables
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(origin)

		for i in range(-2, 3):
			for j in range(-2, 3):
				try:
					if index_A+j < 0 or index_B+i < 0:
						raise IndexError
					elif j % 2 == 0 and (i == -2 or i == 2):
						raise IndexError
					elif (i==-1 or i==1) and (j>=-1 and j<=1):
						raise IndexError
					elif (i==0 and j!=0):
						raise IndexError
					elif self.__myGlobalMatrix[index_A+j][index_B+i] == object.locationID:
						raise IndexError
					elif self.__myPieceMatrix[index_A+j][index_B+i] != "**":
						self.captureAble(self.__myPieceMatrix[index_A+j][index_B+i], object)
					else:
						object.moveSet.add(self.__myGlobalMatrix[index_A+j][index_B+i])
				except IndexError:
					continue
	
	def rookMoveCalc(self, origin, object):
		##Reset
		if "QUEEN" not in object.myID:
			object.moveSet = set()

		##Local Variables
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(origin)
		
		## Horizontal Movement
		for west in range(index_A-1, -1, -1):
			myLoc = self.__myPieceMatrix[west][index_B]
			if myLoc != "**":
				self.captureAble(myLoc, object)
				break
				# if "KING" in self.__activeLocaiton[myLoc].myID:
				# 	continue
				# else:
				# 	break
			object.moveSet.add(self.__myGlobalMatrix[west][index_B])

		for east in range(index_A+1, 8):
			myLoc = self.__myPieceMatrix[east][index_B] 
			if myLoc != "**":
				self.captureAble(myLoc, object)
				break
				# if "KING" in self.__activeLocaiton[myLoc].myID:
				# 	continue
				# else:
				# 	break
			object.moveSet.add(self.__myGlobalMatrix[east][index_B])

		## Vertical Movment
		for north in range(index_B-1, -1, -1):
			myLoc = self.__myPieceMatrix[index_A][north]
			if myLoc != "**":
				self.captureAble(myLoc, object)
				break
				# if "KING" in self.__activeLocaiton[myLoc].myID:
				# 	continue
				# else:
				# 	break
			object.moveSet.add(self.__myGlobalMatrix[index_A][north])
		
		for south in range(index_B+1, 8):
			myLoc = self.__myPieceMatrix[index_A][south]
			if myLoc != "**":
				self.captureAble(myLoc, object)
				# break
				# if "KING" in self.__activeLocaiton[myLoc].myID:
				# 	continue
				# else:
				# 	break
			object.moveSet.add(self.__myGlobalMatrix[index_A][south])
	
	def queenMoveCalc(self, origin, object):
		object.moveSet = set()
		self.bishopMoveCalc(origin, object)
		self.rookMoveCalc(origin, object)

	def endOfGame(self, object):
		if object.locationID in object.threats or object.locationID in object.dangerZone:
			object.inCheck = True
		else:
			object.inCheck = False
	
	def nonKingMoves(self, kingObj, ):
		# print(f"\n{kingObj.myID} = Curr King")
		##Reset
		kingObj.dangerZone = set()

		##Calulates potential threats to king
		for object in self.__activeLocaiton.values():
			if kingObj.myID[-2] != object.myID[-2]:
				if "PAWN" not in object.myID:
					# print(object.myID)
					self.findMyNextMoves(object, calcKing=False)
					for loc in object.moveSet:
						kingObj.dangerZone.add(loc)
				else:
					pawnAttack = self.pawnAttackCalc(object.locationID, object)
					# print(f"{object.myID} attacks {pawnAttack}")
					for loc in pawnAttack:
						# print(loc, "Pawn Attack?")
						kingObj.dangerZone.add(loc)


	def kingMoveCalc(self, origin, object):
		##Rests
		self.nonKingMoves(object)
		object.moveSet = set()
		object.threats = set()
		
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(origin)
		for i in range(-1, 2):
			for j in range(-1, 2):
				try:
					locationUsed = self.__myPieceMatrix[index_A+i][index_B+j]
					globLocation = self.__myGlobalMatrix[index_A+i][index_B+j]
					if (index_A+i) < 0 or (index_B+j) < 0:
						raise IndexError("Less than 0")
					elif globLocation not in object.dangerZone and locationUsed == "**":
						object.moveSet.add(globLocation)
					elif locationUsed != "**":
						self.captureAble(locationUsed, object) ##Only add location as a move, if it's an opposing piece
					else:
						object.threats.add(globLocation)
					if object.locationID in object.dangerZone:
						object.threats.add(object.locationID)
				except IndexError as e:
					# print(e)
					continue
		# print("Next Step?", object.moveSet, object.threats)
		# if len(object.threats) >= 1:
		# 	if object.locationID in object.dangerZone:
		# 		pass
		# self.endOfGame(object)
		# print(object.threats, "Listed Threats")

	def pawnAttackCalc(self, origin, object):
		row = origin[1]
		tempSet = set()

		##Local Variables
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(origin)
		if "-W" in object.myID:
			try: ##Handles Pawn Attacks
				tempSet.add(self.__myGlobalMatrix[index_A-1][index_B+1])
				tempSet.add(self.__myGlobalMatrix[index_A+1][index_B+1])
			except IndexError:
				pass
		elif "-B" in object.myID:
			try: ##Handles Pawn Attacks
				tempSet.add(self.__myGlobalMatrix[index_A-1][index_B-1])
				tempSet.add(self.__myGlobalMatrix[index_A+1][index_B-1])
			except IndexError:
				pass

		return tempSet

	def pawnMoveCalc(self, origin, object):
		##New Call Resets
		currRow = origin[1]
		object.moveSet = set()

		##Local Variables
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(origin)

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
					self.captureAble(self.__myGlobalMatrix[index_A-1][index_B+1], object)
				if self.__myPieceMatrix[index_A+1][index_B+1] != "**":
					self.captureAble(self.__myGlobalMatrix[index_A+1][index_B+1], object)
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
					self.captureAble(self.__myGlobalMatrix[index_A-1][index_B-1], object)
				if self.__myPieceMatrix[index_A+1][index_B-1] != "**":
					self.captureAble(self.__myGlobalMatrix[index_A+1][index_B-1], object)
			except IndexError:
				pass
	


