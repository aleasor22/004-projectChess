##Imports
# from blank import BLANK

class LOGIC:
	def __init__(self, chess):
		self._chess = chess
		self.pieces = {} ##Key == PieceID, value == PIECE.object
		self._myGlobalMatrix = chess.MATRIX.get_matrix("Global")
		self._myPieceMatrix = chess.MATRIX.get_matrix("Piece")
		
		self.turnOrder = ["-W", "-B"]

		##Direction from selected piece to target king 
			##North == row 8
			##South == row 1
			##East == Col h
			##West == Col a
		self.dir = []

	def updateActiveLocaitons(self, object):
		self.pieces[object.myID] = object

	def directionLocaitons(self, myLoc):
		##Locaitons in a certain direction
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(myLoc)
		##Resets
		northWest = []
		north = []
		northEast = []
		southWest = []
		south = []
		southEast = []
		west = []
		east = []
		# print("Center loc:", myLoc)


		for row in range(8):
			for col in range(8):
				matrixLoc = self._myGlobalMatrix[col][row]
				##North/South logic
				if index_A == col:
					if index_B < row: ##South
						south.append(matrixLoc)
					elif index_B > row: ##North
						north.append(matrixLoc)
				elif index_A != col:
					##North East/West Logic
					if index_B > row: ##North
						if index_A < col: ##West
							northWest.append(matrixLoc)
						elif index_A > col: ##East
							northEast.append(matrixLoc)

					##South East/West Logic
					elif index_B < row: ##South
						if index_A < col: ##West
							southWest.append(matrixLoc)
						elif index_A > col: ##East
							southEast.append(matrixLoc)
						
				##East/West Logic
				elif index_B == row:
					if index_A < col: ##West
						west.append(matrixLoc)
					elif index_A > col: ##East
						east.append(matrixLoc)

		## Returns a tuple, Each of the 8 Direcitons are in clockwise order, 
		## Starting from NW, ending w/ West
		return (northWest, north, northEast, east, southEast, south, southWest, west)

	def isCheckmate(self, kingObj):
		protectors = [] ##Pieces that can block for the king get added to this
		print(kingObj.moveSet, "KINGS moveSet")
		for object in self.pieces.values():
			if kingObj.myID[-2] == object.myID[-2] and "KING" not in object.myID:
				self.findMyNextMoves(object, calcKing=False)
				if len(object.moveSet) >= 1:
					protectors.append(object)
		
		if len(protectors) < 1 and len(kingObj.moveSet) < 1:
			print("CHECKMATE")



	def createDangerZone(self, kingObj, otherObj=None):
		kingObj.dangerZone = set()
		if len(kingObj.attackers) >= 1:
			dirCalc = self.directionLocaitons(kingObj.attackers[0].locationID)
		else:
			if otherObj != None:
				dirCalc = self.directionLocaitons(otherObj.locationID)

		if kingObj.locationID in dirCalc[0]:
			self.dir = dirCalc[0]
		if kingObj.locationID in dirCalc[1]:
			self.dir = dirCalc[1]
		if kingObj.locationID in dirCalc[2]:
			self.dir = dirCalc[2]
		if kingObj.locationID in dirCalc[4]:
			self.dir = dirCalc[4]
		if kingObj.locationID in dirCalc[5]:
			self.dir = dirCalc[5]
		if kingObj.locationID in dirCalc[6]:
			self.dir = dirCalc[6]
		if kingObj.locationID in dirCalc[7]:
			self.dir = dirCalc[7]
		if kingObj.locationID in dirCalc[3]:
			self.dir = dirCalc[3]

		# print(f"What is direction: {self.dir}")
		for object in kingObj.attackers:
			kingObj.dangerZone.add(object.locationID)
			for location in object.moveSet:
				if location in self.dir:
					kingObj.dangerZone.add(location)
			
		# print(f"{kingObj.myID}.dangerZone is: {kingObj.dangerZone}")
	
	def attackingTheKing(self, kingID):
		# print(f"\n{kingID} = Curr King")
		##Reset
		kingObj = self.pieces[kingID]
		kingObj.attackers = []
		# kingObj.threats = set()

		##Calulates threats to king
		for object in self.pieces.values():
			if kingObj.myID[-2] != object.myID[-2]:
				self.findMyNextMoves(object, calcKing=False)
				# print(f"{object.myID} attacks {object.moveSet}")
				if kingObj.locationID in object.moveSet:
					kingObj.attackers.append(object)

		# print(kingObj.locationID, "in danger:", kingObj.dangerZone)
		if len(kingObj.attackers) >= 1:
			print(f"Attackers: {kingObj.attackers}")
			self.createDangerZone(kingObj)
			kingObj.inCheck = True
			self.isCheckmate(kingObj)
		else:
			kingObj.inCheck = False

	def potentialThreatsOnKing(self, kingObj):
		kingObj.threats = set()

		##Calulates potential threats to king
		for object in self.pieces.values():
			if kingObj.myID[-2] != object.myID[-2]:
				self.findMyNextMoves(object, calcKing=False)
				if "PAWN" not in object.myID:
					# print(f"{object.myID} attacks {object.moveSet}")
					for loc in object.moveSet:
						kingObj.threats.add(loc)
				else:
					pawnAttack = self.pawnAttackCalc(object.locationID, object)
					for loc in pawnAttack:
						kingObj.threats.add(loc)
	
	##To be used for ROOK, BISHOP, QUEEN move logic
	def directionLooping(self, origin, object, direction):

		##Findes matrix indexes A & B
		globalMatrix = self._chess.MATRIX.get_matrix("Global")
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)
		step_Col, step_Row = (0, 0) ##Default steps 0 columns/rows

		if direction == "North West":
			step_Col, step_Row = (-1, 1)
		elif direction == "North":
			step_Col, step_Row = (1, 0)
		elif direction == "North East":
			step_Col, step_Row = (1, 1)
		elif direction == "East":
			step_Col, step_Row = (0, 1)
		elif direction == "South East":
			step_Col, step_Row = (-1, 1)
		elif direction == "South":
			step_Col, step_Row = (-1, 0)
		elif direction == "South West":
			step_Col, step_Row = (-1, -1)
		elif direction == "West":
			step_Col, step_Row = (0, -1)
		
		for i in range(8):
			try:
				index_A += step_Col
				index_B += step_Row
				if index_A < 0 or index_B < 0:
					raise IndexError("Out of Range - IGNORE")
				
				##object.moveSet logic here
				
			except IndexError as E:
				print(f"ERROR @LOGIC.directionLooping: \n{E}")
	
	##This will be used for pinned Piece Calulations
	def whoIsPinned(self, origin, object, direction, color="black"):

		##Findes matrix indexes A & B
		globalMatrix = self._chess.MATRIX.get_matrix("Global")
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)
		step_Col, step_Row = (0, 0) ##Default steps 0 columns/rows

		if direction == "North West":
			step_Col, step_Row = (-1, 1)
		elif direction == "North":
			step_Col, step_Row = (1, 0)
		elif direction == "North East":
			step_Col, step_Row = (1, 1)
		elif direction == "East":
			step_Col, step_Row = (0, 1)
		elif direction == "South East":
			step_Col, step_Row = (-1, 1)
		elif direction == "South":
			step_Col, step_Row = (-1, 0)
		elif direction == "South West":
			step_Col, step_Row = (-1, -1)
		elif direction == "West":
			step_Col, step_Row = (0, -1)
		
		##Local Variables - May become class variables later
		pieceList = []
		acceptableMoves = []

		for i in range(8):
			try:
				index_A += step_Col
				index_B += step_Row
				if index_A < 0 or index_B < 0:
					raise IndexError("Out of Range - IGNORE")
				# x, y = self._chess.get_nwCoord(globalMatrix[index_A][index_B])
				# self._chess.get_canvas().create_oval(x, y, x+16, y+16, fill=color)
				acceptableMoves.append(globalMatrix[index_A][index_B])
				isPiece = self.get_pieceAtLocation(globalMatrix[index_A][index_B])
				if isPiece != None:
					pieceList.append(isPiece)
					if len(pieceList) >= 2: #NOTE# or self.turnOrder[0] not in isPiece.myID:
						return (pieceList, acceptableMoves)

			except IndexError as E:
				# print(f"ERROR @LOGIC.directionLooping: \n{E}")
				pass

	
	def pinnedPieces(self, kingObj): ##selected, theirKing):
		# print(f"\n{kingObj.myID} pinned Pieces?")
		##All direcitons
		list = ["North West", "North", "North East", "East", 
				"South East", "South", "South West", "West"]
		
		##Determins if a piece is pinned in any of the above directions
		for direction in list:
			temp = self.whoIsPinned(kingObj.locationID, kingObj, direction, "blue")
			if temp != None:
				whosPinned = temp[0]
				allowedMoves = temp[1]
				if kingObj.myID[-2] == whosPinned[0].myID[-2] and kingObj.myID[-2] != whosPinned[1].myID[-2]:
					if "PAWN" in whosPinned[1].myID or "KNIGHT" in whosPinned[1].myID or "KING" in whosPinned[1].myID:
						##Above is True if a Pawn, Knight, or King is the second piece found in this calculation
						pass
					else:
						##When a Queen, Rook, or bishop is the second piece found in this calulation
						# print(f"determine who is pinned: [{whosPinned[0].myID}, {whosPinned[1].myID}]")
						whosPinned[0].isPinned = True
						whosPinned[0].pinnedMoves = allowedMoves

	##Simply turns all opponent pieces pinned logic to false		
	def pinnedPiecesReset(self, kingObj):
		for object in self.pieces.values():
			if kingObj.myID[-2] != object.myID[-2]:
				object.isPinned = False
	
	def isGuarded(self, currObject):
		for object in self.pieces.values():
			if currObject.myID[-2] == object.myID[-2] and object != currObject:
				self.findMyNextMoves(object, calcKing=False)


		return True
	
	def specialMoves(self, location, object):
		
		##Is this location occupied
		foundPiece = self.get_pieceAtLocation(location)
		
		##Force Moves?
		if self.pieces["KING-W0"].inCheck: 
			currKing = self.pieces["KING-W0"]
		elif self.pieces["KING-B0"].inCheck: 
			currKing = self.pieces["KING-B0"]
		else:
			currKing = None

		##Checks if the curr piece - object - is pinned
		if object.isPinned:
			# print(f"{object.myID} is in {object.pinnedMoves}")
			if location in object.pinnedMoves and location != object.locationID:
				object.moveSet.add(location)
		##Check Logic
		elif currKing != None:
			##Forcing other Pieces to protect the king
			if currKing.myID[-2] == object.myID[-2] and location in currKing.dangerZone:
				if location != currKing.locationID:
					object.moveSet.add(location)
				for attacker in currKing.attackers:
					# print(f"{location} vs {attacker.locationID}")
					if location == attacker.locationID and self.isGuarded(attacker):
						object.moveSet.add(location)
		elif foundPiece != None:
			# print(f"{foundPiece.myID}@{foundPiece.locationID}, @specialMoves")
			# print(f"{object.myID[-2]} != {foundPiece.myID[-2]}")
			if object.myID[-2] not in foundPiece.myID[-2]:
				object.moveSet.add(location)
		##Default
		else:
			object.moveSet.add(location)

	def pawnAttackCalc(self, origin, object):
		tempSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(origin)
		if "-W" in object.myID:
			try: ##Handles Pawn Attacks
				tempSet.add(self._myGlobalMatrix[index_A-1][index_B+1])
				tempSet.add(self._myGlobalMatrix[index_A+1][index_B+1])
			except IndexError:
				pass
		elif "-B" in object.myID:
			try: ##Handles Pawn Attacks
				tempSet.add(self._myGlobalMatrix[index_A-1][index_B-1])
				tempSet.add(self._myGlobalMatrix[index_A+1][index_B-1])
			except IndexError:
				pass
		return tempSet
	
	def get_pieceAtLocation(self, location=None):
		"""Returns Piece object @ given location"""
		# print(f"Got Called  @{location}")
		if self._chess.MATRIX.foundInMatrix(location):
			for key, value in self.pieces.items():
				if value.locationID == location:
					# print(f"Found {self.allPieces[key].myID} at {location}")
					return self.pieces[key]
		else:
			print(f"Incorrect Location: {location}")