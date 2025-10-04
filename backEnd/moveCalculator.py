

class MOVECALC():
	def __init__(self, chess, ): ##place):
		##Class Variables (w/ Instance Tracking)
		self.__chess = chess
		self.__myGlobalMatrix = chess.MATRIX.get_matrix("Global")
		self.__myPieceMatrix = chess.MATRIX.get_matrix("Piece")
		self.__activeLocation = {} ##Key == PieceID, value == PIECE.object @ Location

		##Check/Checkmate Logic
		self.WKingCheck = False
		self.BKingCheck = False
	
	def forceThisMove(self, loc, object):
		currKing = None
		if self.__activeLocation["KING-W0"].inCheck:
			currKing = self.__activeLocation["KING-W0"]
		elif self.__activeLocation["KING-B0"].inCheck:
			currKing = self.__activeLocation["KING-B0"]

		# try: ##NOTE: For Debuggin
		# 	print(currKing.myID)
		# except AttributeError:
		# 	print("currKing can't be None")

		##Force this move
		if currKing != None and object.myID[-2] == currKing.myID[-2]:
			if loc in currKing.dangerZone:
				# print("\nNew loc:")
				# # print(f"{currKing.dangerZone}")
				# print(f"{object.myID}'s location: {loc}")
				# print(f"This location: {loc} is found in {currKing.myID}'s dangerZone")
				object.moveSet.add(loc)
				raise IndexError


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
	
	def addActiveLocaitons(self, object):
		self.__activeLocation[object.myID] = object
		# print(f"{object.myID} added to activeLocation[{location}]")

	def captureAble(self, location, object=None):
		"""If the neiboring location is used by an opponent's piece, add it to possible moves"""
		# print(object.myID[-2], " vs ", self.__activeLocation[location].myID[-2])
		for key, value in  self.__activeLocation.items():
			if location == value.locationID:
				break
		if object.myID[-2] not in self.__activeLocation[key].myID[-2]:
			object.moveSet.add(location)

	def bishopMoveCalc(self, origin, object):
		##Resets List
		if "QUEEN" not in object.myID:
			object.moveSet = set()

		##Local Variables
		index_A, index_B = self.__chess.MATRIX.findMatrixIndex(origin)
		myBool = (self.__activeLocation["KING-W0"].inCheck or self.__activeLocation["KING-B0"].inCheck)

		for northEast in range(8):
			try:
				myLoc = self.__myPieceMatrix[index_A+northEast][index_B-northEast]
				myglobLoc = self.__myGlobalMatrix[index_A+northEast][index_B-northEast]
				if index_B-northEast < 0:
					break
				elif myLoc == object.locationID:
					continue
				elif myBool:
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					break
				else:
					object.moveSet.add(self.__myGlobalMatrix[index_A+northEast][index_B-northEast])
			except IndexError as e:
				# print(e)
				break
		for northWest in range(8):
			try:
				myLoc = self.__myPieceMatrix[index_A-northWest][index_B-northWest]
				myglobLoc = self.__myGlobalMatrix[index_A-northWest][index_B-northWest]
				if index_A-northWest < 0 or index_B-northWest < 0:
					raise IndexError("Index Less than 0")
				elif myLoc == object.locationID:
					continue
				elif myBool:
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					raise IndexError
				else:
					object.moveSet.add(self.__myGlobalMatrix[index_A-northWest][index_B-northWest])
			except IndexError as e:
				# print(e)
				break
		for southEast in range(8):
			try:
				myLoc = self.__myPieceMatrix[index_A+southEast][index_B+southEast]
				myglobLoc = self.__myGlobalMatrix[index_A+southEast][index_B+southEast]
				if myLoc == object.locationID:
					continue
				elif myBool:
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					raise IndexError
				else:
					object.moveSet.add(self.__myGlobalMatrix[index_A+southEast][index_B+southEast])
			except IndexError as e:
				# print(e)
				break
		for southWest in range(8):
			try:
				myLoc = self.__myPieceMatrix[index_A-southWest][index_B+southWest]
				myglobLoc = self.__myGlobalMatrix[index_A-southWest][index_B+southWest]
				if index_A-southWest < 0:
					raise IndexError("Index Less than 0")
				elif myLoc == object.locationID:
					continue
				elif myBool:
					self.forceThisMove(myglobLoc, object)
					continue
				elif myLoc != "**": 
					self.captureAble(myLoc, object)
					raise IndexError
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
		myBool = (self.__activeLocation["KING-W0"].inCheck or self.__activeLocation["KING-B0"].inCheck)

		for i in range(-2, 3):
			for j in range(-2, 3):
				try:
					myLoc = self.__myPieceMatrix[index_A+j][index_B+i]
					myglobLoc = self.__myGlobalMatrix[index_A+j][index_B+i]
					
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
					elif myBool:
						self.forceThisMove(myglobLoc, object)
						continue
					elif myLoc != "**":
						self.captureAble(self.__myPieceMatrix[index_A+j][index_B+i], object)
						continue
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
		myBool = (self.__activeLocation["KING-W0"].inCheck or self.__activeLocation["KING-B0"].inCheck)
		
		## Horizontal Movement
		# try:
		for west in range(index_A-1, -1, -1):
			myLoc = self.__myPieceMatrix[west][index_B]
			myglobLoc = self.__myGlobalMatrix[west][index_B]
			try:
				if myBool:
					self.forceThisMove(myglobLoc, object)
					continue
			except IndexError:
				break
			if myLoc != "**":
				self.captureAble(myLoc, object)
				break
			object.moveSet.add(self.__myGlobalMatrix[west][index_B])

		for east in range(index_A+1, 8):
			myLoc = self.__myPieceMatrix[east][index_B] 
			myglobLoc = self.__myGlobalMatrix[east][index_B]
			try:
				if myBool:
					self.forceThisMove(myglobLoc, object)
					continue
			except IndexError:
				break
			if myLoc != "**":
				self.captureAble(myLoc, object)
				break
			object.moveSet.add(self.__myGlobalMatrix[east][index_B])

		## Vertical Movment
		for north in range(index_B-1, -1, -1):
			myLoc = self.__myPieceMatrix[index_A][north]
			myglobLoc = self.__myGlobalMatrix[index_A][north]
			try:
				if myBool:
					self.forceThisMove(myglobLoc, object)
					continue
			except IndexError:
				break
			if myLoc != "**":
				self.captureAble(myLoc, object)
				break
			object.moveSet.add(self.__myGlobalMatrix[index_A][north])
		
		for south in range(index_B+1, 8):
			myLoc = self.__myPieceMatrix[index_A][south]
			myglobLoc = self.__myGlobalMatrix[index_A][south]
			try:
				if myBool:
					self.forceThisMove(myglobLoc, object)
					continue
			except IndexError:
				break
			if myLoc != "**":
				self.captureAble(myLoc, object)
				break
			object.moveSet.add(self.__myGlobalMatrix[index_A][south])
	
	def queenMoveCalc(self, origin, object):
		object.moveSet = set()
		self.bishopMoveCalc(origin, object)
		self.rookMoveCalc(origin, object)

	# def endOfGame(self, object):
	# 	print(f"{object.myID}:", object.locationID in object.threats, object.locationID in object.dangerZone)
	# 	if object.locationID in object.threats or object.locationID in object.dangerZone:
	# 		object.inCheck = True
	# 	else:
	# 		object.inCheck = False

	
	def nonKingMoves(self, kingObj, ):
		# print(f"\n{kingObj.myID} = Curr King")
		##Reset
		kingObj.dangerZone = set()

		##Calulates potential threats to king
		for object in self.__activeLocation.values():
			if kingObj.myID[-2] != object.myID[-2]:
				if "PAWN" not in object.myID:
					self.findMyNextMoves(object, calcKing=False)
					# print(f"{object.myID} attacks {object.moveSet}")
					for loc in object.moveSet:
						kingObj.dangerZone.add(loc)
				else:
					pawnAttack = self.pawnAttackCalc(object.locationID, object)
					# print(f"{object.myID} attacks {pawnAttack}")
					for loc in pawnAttack:
						# print(loc, "Pawn Attack?")
						kingObj.dangerZone.add(loc)
		
		# print(kingObj.locationID, "in danger:", kingObj.dangerZone)
		if kingObj.locationID in kingObj.dangerZone:
			
			kingObj.inCheck = True
		else:
			kingObj.inCheck = False

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
					elif locationUsed != "**" and locationUsed not in object.dangerZone:
							self.captureAble(locationUsed, object) ##Only add location as a move, if it's an opposing piece
					else:
						object.threats.add(globLocation)
					##Adds King's own location to .treats if it's being attacted. 
					if object.locationID in object.dangerZone:
						object.threats.add(object.locationID)
					# 	object.inCheck = True
					# else:
					# 	object.inCheck = False
					
				except IndexError as e:
					# print(e)
					continue
		print(object.threats)

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
			myloc = self.__myPieceMatrix[index_A][index_B+1]
			try: #Handles General Pawn Movement
				if myloc == "**":
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
	


