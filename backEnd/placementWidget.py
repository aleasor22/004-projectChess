#Imports here
# import tkinter
from .Pieces import *


class placements():
	def __init__(self, chess):
		self.__chess = chess
		self.__myGlobalMatrix = chess.MATRIX.get_matrix("Global")
		self.backRow = ["ROOK", "KNIGHT", "BISHOP", "QUEEN", "KING", "BISHOP", "KNIGHT", "ROOK"]
		self.whitePieces = {}
		self.blackPieces = {}


	def createPieces(self, pieceName, quantity, team):
		for pieceNum in range(quantity):
			if team == "white":
				tag = f"{pieceName}-W{pieceNum}"
				self.whitePieces[tag] = self.get_object(pieceName)
				self.whitePieces[tag].myID = tag
				self.whitePieces[tag].myTeam = "white"
			elif team == "black":
				tag = f"{pieceName}-B{pieceNum}"
				self.blackPieces[tag] = self.get_object(pieceName)
				self.blackPieces[tag].myID = tag
				self.blackPieces[tag].myTeam = "black"

	def placePieces(self):
		for row in range(8):
			for col in range(8):
				location = self.__myGlobalMatrix[col][row]
				if row == 0:
					if col <= 4:
						key = f"{self.backRow[col]}-W0"
					elif col > 4:
						key = f"{self.backRow[col]}-W1"
					print(f"Piece Tag: {key}")
					self.whitePieces[key].setup(self.__chess.get_nwCoord(location), "white", location)
				elif row == 1:
					self.whitePieces[f"PAWN-W{col}"].setup(self.__chess.get_nwCoord(location), location)
				elif row == 6:
					self.blackPieces[f"PAWN-B{col}"].setup(self.__chess.get_nwCoord(location), location)
				elif row == 7:
					if col <= 4:
						key = f"{self.backRow[col]}-B0"
					elif col > 4:
						key = f"{self.backRow[col]}-B1"
					print(f"Piece Tag: {key}")
					self.blackPieces[key].setup(self.__chess.get_nwCoord(location), "black", location)

	def movePiece(self, pieceObject, location):
		pos = self.__chess.get_nwCoord(location)
		pieceObject.placeImage(pos[0], pos[1], location)
		pieceObject.availableMoves()

	def capturePiece(self, ):
		pass

	def findNextMoves(self, debugActive=False):
		try:
			##Team White
			for object in self.whitePieces.values():
				object.availableMoves()
				if debugActive:
					print(f"{object.myID} can move here: {object.canMoveHere}")

			print() ##Spacer

			##Team Black
			for object in self.blackPieces.values():
				object.availableMoves()
				if debugActive:
					print(f"{object.myID} can move here: {object.canMoveHere}")
			
		except AttributeError as error:
			print(f"Caught Error:, {error} \n\t @findNextMove()")
		# pass

	def isOpponent(self, currPiece, underPiece):
		print(f"Curr Piece: {currPiece.myTeam}\nCaptured Piece: {underPiece.myTeam}")
		
		
		
		pass


	def get_piece(self, location=None):
		if self.__chess.MATRIX.foundInMatrix(location):
			for key in self.whitePieces.keys():
				if self.whitePieces[key].locationID == location:
					print(f"Found {self.whitePieces[key].myID} at {location}")
					self.whitePieces[key].availableMoves()
					return self.whitePieces[key] 
			for key in self.blackPieces.keys():
				if self.blackPieces[key].locationID == location:
					print(f"Found {self.blackPieces[key].myID} at {location}")
					self.blackPieces[key].availableMoves()
					return self.blackPieces[key] 
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