##Imports
# from blank import BLANK

class LOGIC:
	def __init__(self, chess):
		self._chess = chess
		self._pieces = {} ##Key == PieceID, value == PIECE.object @ Location
		self._myGlobalMatrix = chess.MATRIX.get_matrix("Global")
		self._myPieceMatrix = chess.MATRIX.get_matrix("Piece")
		
		self.turnOrder = ["-W", "-B"]

		##Direction from selected piece to target king 
			##North == row 8
			##South == row 1
			##East == Col h
			##West == Col a
		self.__direction = ""


	def kingDirection(self, selectedPiece, king):
		##Variable Tracking
		colP = selectedPiece.locationID[0]
		rowP = selectedPiece.locationID[1]
		colK = king.locationID[0]
		rowK = king.locationID[1]

		##North/South logic
		if colP == colK:
			if int(rowP) < int(rowK): ##South
				self.__direction = "S"
				pass
			elif int(rowP) > int(rowK): ##North
				self.__direction = "N"
		elif colP != colK:
			##North East/West Logic
			if int(rowP) > int(rowK): ##North
				if colP < colK: ##West
					self.__direction = "NW"
				elif colP > colK: ##East
					self.__direction = "NE"

			##South East/West Logic
			elif int(rowP) < int(rowK): ##South
				if colP < colK: ##West
					self.__direction = "SW"
				elif colP > colK: ##East
					self.__direction = "SE"
				
		##East/West Logic
		elif rowP == rowK:
			if colP < colK: ##West
				self.__direction = "W"
				pass
			elif colP > colK: ##East
				self.__direction = "E"
		else:
			##This should never print
			print("Somthin went wrong @LOGIC.kingDirection")
				
		# print(f"{self.__direction} of {king.myID}")
	
	def nonKingMoves(self, kingID, ):
		# print(f"\n{kingID} = Curr King")
		##Reset
		kingObj = self._pieces[kingID]
		kingObj.dangerZone = set()

		##Calulates potential threats to king
		for object in self._pieces.values():
			if kingObj.myID[-2] != object.myID[-2]:
				self.findMyNextMoves(object, calcKing=False)
				if "PAWN" not in object.myID:
					# print(f"{object.myID} attacks {object.moveSet}")
					for loc in object.moveSet:
						self.kingDirection(object, kingObj)
						kingObj.dangerZone.add(loc)
				else:
					pawnAttack = self.pawnAttackCalc(object.locationID, object)
					# print(f"{object.myID} attacks {pawnAttack}")
					for loc in pawnAttack:
						# print(loc, "Pawn Attack?")
						# self.kingDirection(object, kingObj)
						kingObj.dangerZone.add(loc)
		
		# print(kingObj.locationID, "in danger:", kingObj.dangerZone)
		if kingObj.locationID in kingObj.dangerZone:
			kingObj.inCheck = True
		else:
			kingObj.inCheck = False
	
	# def specialMoves(self, location, object):





	# 	pass
	def captureAble(self, location, object=None):
		"""If the neiboring location is used by an opponent's piece, add it to possible moves"""
		# print(object.myID[-2], " vs ", self._pieces[location].myID[-2])
		# for key, value in  self._pieces.items():
		# 	if location == value.locationID:
		# 		break
		if object.myID[-2] not in self.get_pieceAtLocation(location).myID[-2]:
			object.moveSet.add(location)

	def forceThisMove(self, loc, object):
		currKing = None
		if self._pieces["KING-W0"].inCheck:
			currKing = self._pieces["KING-W0"]
		elif self._pieces["KING-B0"].inCheck:
			currKing = self._pieces["KING-B0"]

		##Force this move
		if currKing != None and object.myID[-2] == currKing.myID[-2]:
			if loc in currKing.dangerZone:
				if "PAWN" in object.myID:
					print(f"{loc} is in {currKing.dangerZone}")
				object.moveSet.add(loc)
				raise IndexError
			else:
				if "PAWN" in object.myID:
					print(f"{object.myID} got missed?")

				
	def pawnAttackCalc(self, origin, object):
		row = origin[1]
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
			for key in self._pieces.keys():
				if self._pieces[key].locationID == location:
					# print(f"Found {self.allPieces[key].myID} at {location}")
					return self._pieces[key]
		else:
			print(f"Incorrect Location: {location}")
	
	def returnKingsInCheck(self):
		return (self._pieces["KING-W0"] or self._pieces["KING-B0"])