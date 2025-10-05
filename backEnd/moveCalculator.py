from .checkLogic import LOGIC

class MOVECALC(LOGIC):
	def __init__(self, chess, ): ##place):
		##Class Variables (w/ Instance Tracking)
		LOGIC.__init__(self, chess)
		self.turnOrder = ["-W", "-B"]


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
	
	def addActiveLocaitons(self, key, object):
		self._pieces[key] = object
		# print(f"{object.myID} added to activeLocation[{location}]")

	def bishopMoveCalc(self, origin, object):
		##Resets List
		if "QUEEN" not in object.myID:
			object.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)
		myBool = (self._pieces["KING-W0"].inCheck or self._pieces["KING-B0"].inCheck)

		for northEast in range(8):
			try:
				myLoc = self._myPieceMatrix[index_A+northEast][index_B-northEast]
				myglobLoc = self._myGlobalMatrix[index_A+northEast][index_B-northEast]
				if index_B-northEast < 0:
					break
				elif myLoc == object.locationID:
					continue
				elif myBool  and self.turnOrder[0] not in object.myID:
					if myLoc != "**":
						break
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					break
				else:
					object.moveSet.add(self._myGlobalMatrix[index_A+northEast][index_B-northEast])
			except IndexError as e:
				# print(e)
				break
		for northWest in range(8):
			try:
				myLoc = self._myPieceMatrix[index_A-northWest][index_B-northWest]
				myglobLoc = self._myGlobalMatrix[index_A-northWest][index_B-northWest]
				if index_A-northWest < 0 or index_B-northWest < 0:
					raise IndexError("Index Less than 0")
				elif myLoc == object.locationID:
					continue
				elif myBool  and self.turnOrder[0] not in object.myID:
					if myLoc != "**":
						break
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					raise IndexError
				else:
					object.moveSet.add(self._myGlobalMatrix[index_A-northWest][index_B-northWest])
			except IndexError as e:
				# print(e)
				break
		for southEast in range(8):
			try:
				myLoc = self._myPieceMatrix[index_A+southEast][index_B+southEast]
				myglobLoc = self._myGlobalMatrix[index_A+southEast][index_B+southEast]
				if myLoc == object.locationID:
					continue
				elif myBool  and self.turnOrder[0] not in object.myID:
					if myLoc != "**":
						break
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					raise IndexError
				else:
					object.moveSet.add(self._myGlobalMatrix[index_A+southEast][index_B+southEast])
			except IndexError as e:
				# print(e)
				break
		for southWest in range(8):
			try:
				myLoc = self._myPieceMatrix[index_A-southWest][index_B+southWest]
				myglobLoc = self._myGlobalMatrix[index_A-southWest][index_B+southWest]
				if index_A-southWest < 0:
					raise IndexError("Index Less than 0")
				elif myLoc == object.locationID:
					continue
				elif myBool and self.turnOrder[0] not in object.myID:
					if myLoc != "**":
						break
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					raise IndexError
				else:
					object.moveSet.add(self._myGlobalMatrix[index_A-southWest][index_B+southWest])
			except IndexError as e:
				# print(e)
				break	
	
	def knightMoveCalc(self, origin, object):
		##Resets
		object.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)
		myBool = (self._pieces["KING-W0"].inCheck or self._pieces["KING-B0"].inCheck)

		for i in range(-2, 3):
			for j in range(-2, 3):
				try:
					myLoc = self._myPieceMatrix[index_A+j][index_B+i]
					myglobLoc = self._myGlobalMatrix[index_A+j][index_B+i]
					
					if index_A+j < 0 or index_B+i < 0:
						continue
					elif j % 2 == 0 and (i == -2 or i == 2):
						continue
					elif (i==-1 or i==1) and (j>=-1 and j<=1):
						continue
					elif (i==0 and j!=0):
						continue
					elif myglobLoc == object.locationID:
						continue
					elif myBool and self.turnOrder[0] not in object.myID:
						self.forceThisMove(myglobLoc, object)
						continue
					elif myLoc != "**":
						self.captureAble(self._myPieceMatrix[index_A+j][index_B+i], object)
						continue
					else:
						object.moveSet.add(self._myGlobalMatrix[index_A+j][index_B+i])
				except IndexError:
					continue
	
	def rookMoveCalc(self, origin, object):
		##Reset
		if "QUEEN" not in object.myID:
			object.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)
		myBool = (self._pieces["KING-W0"].inCheck or self._pieces["KING-B0"].inCheck)
		
		## Horizontal Movement
		for west in range(index_A-1, -1, -1):
			myLoc = self._myPieceMatrix[west][index_B]
			myglobLoc = self._myGlobalMatrix[west][index_B]
			try:
				if myBool and self.turnOrder[0] not in object.myID:
					if myLoc != "**":
						break
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**":
					self.captureAble(myLoc, object)
					break
			except IndexError:
				break
			object.moveSet.add(self._myGlobalMatrix[west][index_B])

		for east in range(index_A+1, 8):
			myLoc = self._myPieceMatrix[east][index_B] 
			myglobLoc = self._myGlobalMatrix[east][index_B]
			try:
				if myBool and self.turnOrder[0] not in object.myID:
					if myLoc != "**":
						break
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**":
					self.captureAble(myLoc, object)
					break
			except IndexError:
				break
			object.moveSet.add(self._myGlobalMatrix[east][index_B])

		## Vertical Movment
		for north in range(index_B-1, -1, -1):
			myLoc = self._myPieceMatrix[index_A][north]
			myglobLoc = self._myGlobalMatrix[index_A][north]
			try:
				if myBool and self.turnOrder[0] not in object.myID:
					if myLoc != "**":
						break
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**":
					self.captureAble(myLoc, object)
					break
			except IndexError:
				break
			object.moveSet.add(myglobLoc)
		
		for south in range(index_B+1, 8):
			myLoc = self._myPieceMatrix[index_A][south]
			myglobLoc = self._myGlobalMatrix[index_A][south]			
			try:
				if myBool and self.turnOrder[0] not in object.myID:
					if myLoc != "**":
						break
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**":
					self.captureAble(myLoc, object)
					break
			except IndexError:
				break
			object.moveSet.add(self._myGlobalMatrix[index_A][south])
	
	def queenMoveCalc(self, origin, object):
		object.moveSet = set()
		self.bishopMoveCalc(origin, object)
		self.rookMoveCalc(origin, object)

	def kingMoveCalc(self, origin, object):
		##Rests
		self.nonKingMoves(object.myID)
		object.moveSet = set()
		object.threats = set()
		
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)
		for i in range(-1, 2):
			for j in range(-1, 2):
				try:
					locationUsed = self._myPieceMatrix[index_A+i][index_B+j]
					globLocation = self._myGlobalMatrix[index_A+i][index_B+j]
					if (index_A+i) < 0 or (index_B+j) < 0:
						raise IndexError("Less than 0")
					elif globLocation not in object.dangerZone and locationUsed == "**":
						object.moveSet.add(globLocation)
					elif locationUsed != "**" and locationUsed not in object.dangerZone:
						self.captureAble(locationUsed, object) ##Only add location as a move, if it's an opposing piece
					else:
						# print(object.dangerZone)
						object.threats.add(globLocation)
					##Adds King's own location to .treats if it's being attacted. 
					if object.locationID in object.dangerZone:
						object.threats.add(object.locationID)					
				except IndexError as e:
					print(e)
					continue

	def pawnMoveCalc(self, origin, object):
		##New Call Resets
		currRow = origin[1]
		object.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)
		myBool = (self._pieces["KING-W0"].inCheck or self._pieces["KING-B0"].inCheck)

		if "-W" in object.myID:
			myloc = self._myPieceMatrix[index_A][index_B+1]
			try: #Handles General Pawn Movement
				if myloc == "**":
					if myBool and self.turnOrder[0] not in object.myID:
						self.forceThisMove(self._myGlobalMatrix[index_A][index_B+1], object)
					else:
						object.moveSet.add(self._myGlobalMatrix[index_A][index_B+1])
				if currRow == "2" and self._myPieceMatrix[index_A][index_B+2] == "**":
					if myBool and self.turnOrder[0] not in object.myID:
						self.forceThisMove(self._myGlobalMatrix[index_A][index_B+2], object)
					else:
						object.moveSet.add(self._myGlobalMatrix[index_A][index_B+2])
			except IndexError:
				pass
			try: ##Handles Pawn Attacks
				if self._myPieceMatrix[index_A-1][index_B+1] != "**":
					self.captureAble(self._myGlobalMatrix[index_A-1][index_B+1], object)
				if self._myPieceMatrix[index_A+1][index_B+1] != "**":
					self.captureAble(self._myGlobalMatrix[index_A+1][index_B+1], object)
			except IndexError:
				pass
		if "-B" in object.myID:
			try: #Handles General Pawn Movement
				if self._myPieceMatrix[index_A][index_B-1] == "**":
					if myBool and self.turnOrder[0] not in object.myID:
						self.forceThisMove(self._myGlobalMatrix[index_A][index_B-1], object)
					else:
						object.moveSet.add(self._myGlobalMatrix[index_A][index_B-1])
				if currRow == "7" and self._myPieceMatrix[index_A][index_B-2] == "**":
					if myBool and self.turnOrder[0] not in object.myID:
						self.forceThisMove(self._myGlobalMatrix[index_A][index_B-2], object)
					else:
						object.moveSet.add(self._myGlobalMatrix[index_A][index_B-2])
			except IndexError:
				pass
			try: ##Handles Pawn Attacks
				if self._myPieceMatrix[index_A-1][index_B-1] != "**":
					self.captureAble(self._myGlobalMatrix[index_A-1][index_B-1], object)
				if self._myPieceMatrix[index_A+1][index_B-1] != "**":
					self.captureAble(self._myGlobalMatrix[index_A+1][index_B-1], object)
			except IndexError:
				pass
	


