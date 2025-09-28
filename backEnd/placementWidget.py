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
		self.originalID = None
		self.oldLocation = None
		self.activePiece = False

		##Team Scoring Varibles
		self.blackTeamScore = 0
		self.blackCaptures = []
		self.whiteTeamScore = 0
		self.whiteCaptures = []

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

	##Places a star next to a selected piece
	def selectPiece(self, currMouseLoc):
		try:
			self.selectedPiece = self.get_piece(currMouseLoc)
			if self.turnOrder[0] in self.selectedPiece.myID:
				self.selectImg.removeImage()
				self.selectImg.placeImage(currMouseLoc)
				if self.selectedPiece != None:
					self.oldLocation = self.selectedPiece.locationID
					self.originalID = self.selectedPiece.canvasID
					self.selectedPiece.availableMoves()
					self.activePiece = True
			else:
				print("not your turn")
			# self.__chess.MATRIX.printMyPieceMatrix()
		except AttributeError:
			self.activePiece = False

	def nextTurn(self):
		currTurn = self.turnOrder[0]
		self.turnOrder.remove(currTurn)
		self.turnOrder.append(currTurn)

	##Moves the selected piece to next location
	def movePiece(self, location, mousePress=False):
		try:
			pos = self.__chess.get_nwCoord(location)
			self.__chess.get_canvas().coords(self.selectedPiece.canvasID, pos[0], pos[1])
			# self.selectedPiece.locationID = location
			# print(self.selectedPiece.locationID)

			if mousePress:
				if location in self.selectedPiece.canMoveHere:
					self.capturePiece(location)
					self.selectedPiece.placeImage(location)
					self.__chess.MATRIX.updatePieceMatrix(self.oldLocation, location)
					self.nextTurn()
				else:
					self.selectedPiece.placeImage(self.oldLocation)
				self.__chess.get_canvas().delete(self.originalID)
				self.activePiece = False
		except AttributeError:
			# print(f"self.selectedPiece cannot be NoneType \n\t@PLACE.movePiece()")
			pass

	def capturePiece(self, location):
		if self.__chess.MATRIX.foundInPieceMatrix(location):
			for key, value in self.allPieces.items():
				# print(f"{key} = {value}")
				if location == value.locationID:
					currTeam = f"{self.selectedPiece.myID[-3]}{self.selectedPiece.myID[-2]}"
					opponent = f"{key[-3]}{key[-2]}"
					if currTeam != opponent:
						if currTeam == "-W":
							self.whiteCaptures.append(value)
							self.whiteTeamScore += value.piecePoints
							value.removeImage()
						elif currTeam == "-B":
							self.blackCaptures.append(value)
							self.blackTeamScore += value.piecePoints
							value.removeImage()

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