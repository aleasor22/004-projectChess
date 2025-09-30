#Imports here
# import tkinter
from .imageWidget import IMAGE
from .Pieces import *


class placements():
	def __init__(self, chess):
		##Config Variables
		self.__chess = chess
		self.__myGlobalMatrix = chess.MATRIX.get_matrix("Global")
		self.__myPieceMatrix = chess.MATRIX.get_matrix("Piece")
		self.backRow = ["ROOK", "KNIGHT", "BISHOP", "QUEEN", "KING", "BISHOP", "KNIGHT", "ROOK"]
		self.allPieces = {}

		##Piece Selection marker
		self.selectImg = IMAGE(chess)
		self.selectImg.createImage("Images/SelectedPiece.png")

		##Piece Movement Variables
		self.turnOrder = ["-W", "-B"]
		self.selectedPiece = None
		self.activePiece = False
		self.oldLocation = None
		self.originalID = None

		##Piece Capturing Varibles
		self.blackTeamScore = 0
		self.blackCaptures = []
		self.whiteTeamScore = 0
		self.whiteCaptures = []

		##King is Under Threat Variables
		self.kingInCheck = False
		self.WKingUnderThreat = []
		self.BKingUnderThreat = []


	def createPieces(self, pieceName, quantity, team):
		for pieceNum in range(quantity):
			if team == "white":
				tag = f"{pieceName}-W{pieceNum}"
				self.allPieces[tag] = self.get_object(pieceName)
				self.allPieces[tag].myID = tag
			elif team == "black":
				tag = f"{pieceName}-B{pieceNum}"
				self.allPieces[tag] = self.get_object(pieceName)
				self.allPieces[tag].myID = tag

	def placePieces(self):
		for row in range(8):
			for col in range(8):
				location = self.__myGlobalMatrix[col][row]
				if row == 0:
					if col <= 4:
						key = f"{self.backRow[col]}-W0"
					elif col > 4:
						key = f"{self.backRow[col]}-W1"
					# print(f"Piece Tag: {key}")
					self.allPieces[key].setup(location)
				elif row == 1:
					self.allPieces[f"PAWN-W{col}"].setup(location)
				elif row == 6:
					self.allPieces[f"PAWN-B{col}"].setup(location)
				elif row == 7:
					if col <= 4:
						key = f"{self.backRow[col]}-B0"
					elif col > 4:
						key = f"{self.backRow[col]}-B1"
					# print(f"Piece Tag: {key}")
					self.allPieces[key].setup(location)

	def nextTurn(self):
		currTurn = self.turnOrder[0]
		self.turnOrder.remove(currTurn)
		self.turnOrder.append(currTurn)

	##Places a star next to a selected piece
	def selectPiece(self, currMouseLoc):
		try:
			self.selectedPiece = self.get_piece(currMouseLoc)
			if self.turnOrder[0] in self.selectedPiece.myID:
				self.selectImg.removeImage()
				self.selectImg.placeImage(currMouseLoc)
				self.selectedPiece.availableMoves()
				self.selectedPiece.showMyMoves()
				if self.selectedPiece != None:
					# print(f"{self.selectedPiece.myID} can move: {self.selectedPiece.canMoveHere}")
					self.oldLocation = self.selectedPiece.locationID
					self.originalID = self.selectedPiece.canvasID
					self.activePiece = True
			else:
				print(f"not your turn - found Piece: {self.get_piece(currMouseLoc)}")
			# self.__chess.MATRIX.printMyPieceMatrix()
		except AttributeError:
			self.activePiece = False

	##Moves the selected piece to next location
	def movePiece(self, location, mousePress=False):
		try:
			pos = self.__chess.get_nwCoord(location)
			self.__chess.get_canvas().coords(self.selectedPiece.canvasID, pos[0], pos[1])

			if mousePress:
				# print(f"Opponent Found? {self.isOpponent(location)}")
				if location in self.selectedPiece.canMoveHere and self.isOpponent(location) != None:
					self.capturePiece(location)
					self.selectedPiece.placeImage(location)
					self.__chess.MATRIX.updatePieceMatrix(self.oldLocation, location)
					self.selectedPiece.availableMoves()
					self.nextTurn()
				elif self.kingInCheck:
					print("a king is under check")
				else:
					self.selectedPiece.placeImage(self.oldLocation)
				self.selectedPiece.delShownMoves()
				self.__chess.get_canvas().delete(self.originalID)
				self.activePiece = False
		except AttributeError:
			# print(f"self.selectedPiece cannot be NoneType \n\t@PLACE.movePiece()")
			pass

	def capturePiece(self, location):
		self.underPiece = None
		if self.isOpponent(location):
			# print(f"{self.underPiece.myID} is under team {self.turnOrder[0]} \n\t@PLACE.capturePiece")
			if self.turnOrder[0] == "-W":
				self.whiteCaptures.append(self.underPiece)
				self.whiteTeamScore += self.underPiece.piecePoints
				self.removePiece()
			elif self.turnOrder[0] == "-B":
				self.blackCaptures.append(self.underPiece)
				self.blackTeamScore += self.underPiece.piecePoints
				self.removePiece()

	def isOpponent(self, location):
		if self.__chess.MATRIX.foundInPieceMatrix(location):
			for key, value in self.allPieces.items():
				if location == value.locationID:
					underPiece = f"{key[-3]}{key[-2]}"
					# print(f"{self.turnOrder[0]} == {underPiece}")
					if self.turnOrder[0] != underPiece:
						self.underPiece = value
						return True
		else:
			return False
	
	def underCheck(self, ):
		##Resets
		self.WKingUnderThreat = []
		self.BKingUnderThreat = []

		try:
			WKingLocation = self.allPieces["KING-W0"].locationID
			BKingLocation = self.allPieces["KING-B0"].locationID
			if self.turnOrder[0] == "-W":
				for key, value in self.allPieces.items():
					if ("KING" not in key) and ("-W" not in key):
						if WKingLocation in value.canMoveHere:
							print(f"{WKingLocation} found in {value.canMoveHere}")
							self.WKingUnderThreat.append(value)
				
				if len(self.WKingUnderThreat) > 0:
					self.kingInCheck = True
				else:
					self.kingInCheck = False
				

			elif self.turnOrder[0] == "-B":
				for key, value in self.allPieces.items():
					if ("KING" not in key) and ("-B" not in key):
						if BKingLocation in value.canMoveHere:
							print(f"{BKingLocation} found in {value.canMoveHere}")
							self.BKingUnderThreat.append(value)
				
				if len(self.BKingUnderThreat) > 0:
					self.kingInCheck = True
				else:
					self.kingInCheck = False
			
			
		except KeyError as e:
			if "KING-W0" not in self.allPieces.keys() or "KING-B0" not in self.allPieces.keys():
				self.__chess.get_canvas().quit()
				print("Game Over")
			else:
				print(e)
				pass

		def changeLocationColor(self, location, newColor):
			print(f"Change {location} color to: {newColor}")
			self.__chess.get_canvas().itemconfig(self.__chess.bboxInfo[location][0], fill=newColor)
			pass

	def findNextMoves(self, debugActive=False):
		try:
			##Team White
			for object in self.allPieces.values():
				object.availableMoves()
				if debugActive:
					print(f"{object.myID} can move here: {object.canMoveHere}")
			
		except AttributeError as error:
			print(f"Caught Error:, {error} \n\t @findNextMove()")
		# pass

	def get_piece(self, location=None):
		if self.__chess.MATRIX.foundInMatrix(location):
			for key in self.allPieces.keys():
				if self.allPieces[key].locationID == location:
					# print(f"Found {self.allPieces[key].myID} at {location}")
					self.allPieces[key].availableMoves()
					return self.allPieces[key]
		else:
			print(f"Incorrect Location: {location}")

	def get_object(self, title):
		if title == "ROOK": ##ROOK
			return ROOK(self.__chess)
		elif title == "KNIGHT": ##KNIGHT
			return KNIGHT(self.__chess)
		elif title == "BISHOP": ##BISHOP
			return BISHOP(self.__chess)
		elif title == "KING": ##KING
			return KING(self.__chess)
		elif title == "QUEEN": ##QUEEN
			return QUEEN(self.__chess)
		elif title == "PAWN": ##PAWN
			return PAWN(self.__chess)
		else:
			print(f"Incorrect Piece Name: {title} \n")

	def removePiece(self):
		self.underPiece.removeImage()
		del self.allPieces[self.underPiece.myID]
		# print(f"Is {self.underPiece.myID} in self.allPieces? {self.underPiece.myID in self.allPieces.keys()}")