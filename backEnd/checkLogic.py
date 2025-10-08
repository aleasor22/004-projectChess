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
		self.northWest = []
		self.north = []
		self.northEast = []
		self.southWest = []
		self.south = []
		self.southEast = []

	def updateActiveLocaitons(self, object):
		self.pieces[object.myID] = object

	def directionLocaitons(self, myLoc):
		##Locaitons in a certain direction
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(myLoc)
		##Resets
		self.northWest = []
		self.north = []
		self.northEast = []
		self.southWest = []
		self.south = []
		self.southEast = []
		self.west = []
		self.east = []
		# print("Center loc:", myLoc)


		for row in range(8):
			for col in range(8):
				matrixLoc = self._myGlobalMatrix[col][row]
				##North/South logic
				if index_A == col:
					if index_B < row: ##South
						self.south.append(matrixLoc)
					elif index_B > row: ##North
						self.north.append(matrixLoc)
				elif index_A != col:
					##North East/West Logic
					if index_B > row: ##North
						if index_A < col: ##West
							self.northWest.append(matrixLoc)
						elif index_A > col: ##East
							self.northEast.append(matrixLoc)

					##South East/West Logic
					elif index_B < row: ##South
						if index_A < col: ##West
							self.southWest.append(matrixLoc)
						elif index_A > col: ##East
							self.southEast.append(matrixLoc)
						
				##East/West Logic
				elif index_B == row:
					if index_A < col: ##West
						self.west.append(matrixLoc)
					elif index_A > col: ##East
						self.east.append(matrixLoc)

	def createDangerZone(self, kingObj, otherObj=None):
		kingObj.dangerZone = set()
		if len(kingObj.attackers) >= 1:
			self.directionLocaitons(kingObj.attackers[0].locationID)
		else:
			if otherObj != None:
				self.directionLocaitons(otherObj.locationID)

		if kingObj.locationID in self.northWest:
			self.dir = self.northWest
		if kingObj.locationID in self.north:
			self.dir= self.north
		if kingObj.locationID in self.northEast:
			self.dir= self.northEast
		if kingObj.locationID in self.southWest:
			self.dir= self.southWest
		if kingObj.locationID in self.south:
			self.dir= self.south
		if kingObj.locationID in self.southEast:
			self.dir= self.southEast
		if kingObj.locationID in self.west:
			self.dir= self.west
		if kingObj.locationID in self.east:
			self.dir= self.east

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
	
	def pinnedPieced(self, selected, theirKing):
		##Planned Logic for Pinned Pieces		
		pass
	
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

		##Chec/Checkmate Logic
		if currKing != None:
			##Forcing other Pieces to protect the king
			if currKing.myID[-2] == object.myID[-2] and location in currKing.dangerZone:
				if location != currKing.locationID:
					object.moveSet.add(location)
				for attacker in currKing.attackers:
					print(f"{location} vs {attacker.locationID}")
					if location == attacker.locationID:
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
		# print(f"Got Called  @{location}")
		if self._chess.MATRIX.foundInMatrix(location):
			for key, value in self.pieces.items():
				if value.locationID == location:
					# print(f"Found {self.allPieces[key].myID} at {location}")
					return self.pieces[key]
		else:
			print(f"Incorrect Location: {location}")