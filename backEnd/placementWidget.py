#Imports here
# import tkinter
from .imageWidget import IMAGE
from .Pieces import *


class PLACEMENT():
	def __init__(self, chess, calc):
		##Config Variables
		self.__chess = chess
		self.__moveCalc = calc
		self.__myGlobalMatrix = chess.MATRIX.get_matrix("Global")
		self.backRow = ["ROOK", "KNIGHT", "BISHOP", "QUEEN", "KING", "BISHOP", "KNIGHT", "ROOK"]
		self.allPieces = {}

		##Piece Selection marker
		self.selectImg = IMAGE(chess)
		self.selectImg.createImage("Images/SelectedPiece.png")
		self.selectImg.myID = "SELECT"

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
		self.locationChanged = []
		self.kingInCheckTracking = {}


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
					self.__moveCalc.updateActiveLocaitons(location, self.allPieces[key])
				elif row == 1:
					self.allPieces[f"PAWN-W{col}"].setup(location)
					self.__moveCalc.updateActiveLocaitons(location, self.allPieces[f"PAWN-W{col}"])
				elif row == 6:
					self.allPieces[f"PAWN-B{col}"].setup(location)
					self.__moveCalc.updateActiveLocaitons(location, self.allPieces[f"PAWN-B{col}"])
				elif row == 7:
					if col <= 4:
						key = f"{self.backRow[col]}-B0"
					elif col > 4:
						key = f"{self.backRow[col]}-B1"
					# print(f"Piece Tag: {key}")
					self.allPieces[key].setup(location)
					self.__moveCalc.updateActiveLocaitons(location, self.allPieces[key])

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
				if self.selectedPiece != None:
					self.__moveCalc.findMyNextMoves(self.selectedPiece)
					self.selectedPiece.showMyMoves()
					self.oldLocation = self.selectedPiece.locationID
					self.originalID = self.selectedPiece.canvasID
					self.activePiece = True
			else:
				print(f"not your turn - found Piece: {self.get_piece(currMouseLoc).myID}")
			# self.__chess.MATRIX.printMyPieceMatrix()
		except AttributeError as e:
			print(f"No Piece Selected: {e} \n\tPLACE.selectPiece()")
			self.activePiece = False

	##Moves the selected piece to next location
	def movePiece(self, location, mousePress=False):
		try:
			pos = self.__chess.get_nwCoord(location)
			self.__chess.get_canvas().coords(self.selectedPiece.canvasID, pos[0], pos[1])

			if mousePress:
				if location in self.selectedPiece.moveSet:
					self.capturePiece(location)
					self.selectedPiece.placeImage(location)
					self.__chess.MATRIX.updatePieceMatrix(self.oldLocation, location)
					self.__moveCalc.updateActiveLocaitons(location, self.selectedPiece)
					self.nextTurn()
				else:
					self.selectedPiece.placeImage(self.oldLocation)
				self.selectedPiece.delShownMoves()
				self.__chess.get_canvas().delete(self.originalID)
				self.activePiece = False
		except AttributeError as e:
			print(f"Error: {e} \n\t@PLACE.movePiece()")
			pass

	def capturePiece(self, location):
		try:
			self.underPiece = None
			if self.isOpponent(location):
				if self.turnOrder[0] == "-W":
					self.whiteCaptures.append(self.underPiece)
					self.whiteTeamScore += self.underPiece.piecePoints
					self.removePiece()
				elif self.turnOrder[0] == "-B":
					self.blackCaptures.append(self.underPiece)
					self.blackTeamScore += self.underPiece.piecePoints
					self.removePiece()
		except AttributeError as e:
			print(f"Error: {e} \n\tPLACE.capturePiece()")

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
	
	def changeLocationColor(self, key, newColor='default'):
		if newColor != 'default' and key != "":
			self.__chess.get_canvas().itemconfig(self.__chess.bboxInfo[self.allPieces[key].locationID][0], fill=newColor)
			self.locationChanged.append(self.allPieces[key].locationID)
		else:
			for id in self.locationChanged:
				tuple = self.__chess.bboxInfo[id]
				self.__chess.get_canvas().itemconfig(tuple[0], fill=tuple[1])
			self.locationChanged = []
				

	def get_piece(self, location=None):
		# print(f"Got Called  @{location}")
		if self.__chess.MATRIX.foundInMatrix(location):
			for key in self.allPieces.keys():
				if self.allPieces[key].locationID == location:
					# print(f"Found {self.allPieces[key].myID} at {location}")
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