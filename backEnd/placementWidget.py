#Imports here
# import tkinter
from .Pieces import *


class placements():
	def __init__(self, chessObject):
		self.__chessGame = chessObject
		self.__render = chessObject.get_canvas()
		self.__pieceList = [ROOK(chessObject), KNIGHT(chessObject), BISHOP(chessObject), KING(chessObject), QUEEN(chessObject), PAWN(chessObject)]
		self.whitePieces = {}
		self.blackPieces = {}


	def createPieces(self, pieceName, quantity, team):
		for pieceNum in range(quantity):
			tag = f"{pieceName}-{pieceNum}"
			if team == "white":
				self.whitePieces[tag] = self.get_object(pieceName)
				self.whitePieces[tag].myID = tag
				self.whitePieces[tag].myTeam = "white"
			elif team == "black":
				self.blackPieces[tag] = self.get_object(pieceName)
				self.blackPieces[tag].myID = tag
				self.blackPieces[tag].myTeam = "black"



	def placePieces(self, team):
		##Select Team
		if team == "white":
			teamDict = self.whitePieces
			frontRow = 2
			backRow = 1
		elif team == "black":
			teamDict = self.blackPieces
			frontRow = 7
			backRow = 8
		
		pawnCount = 0
		columnNumber = 0
		altColumnNum = 7
		for key in teamDict.keys():
			if "PAWN" not in key:
				if "0" in key:
					location = f"{self.__chessGame.columnTitle[columnNumber]}{backRow}"
					teamDict[key].setup(self.__chessGame.get_nwCoord(location), team, location)
					self.__chessGame.activePositions.append(location)
					columnNumber += 1
				elif "1" in key:
					location = f"{self.__chessGame.columnTitle[altColumnNum]}{backRow}"
					teamDict[key].setup(self.__chessGame.get_nwCoord(location), team, location)
					self.__chessGame.activePositions.append(location)
					altColumnNum -= 1
			else:
				location = f"{self.__chessGame.columnTitle[pawnCount]}{frontRow}"
				teamDict[f"PAWN-{pawnCount}"].setup(self.__chessGame.get_nwCoord(location), team, location)
				self.__chessGame.activePositions.append(location)
				pawnCount += 1

	def place(self, pieceObject, location):
		position = self.__chessGame.get_nwCoord(location)
		pieceObject.placeImage(position[0], position[1], location)
		pieceObject.availableMoves() ##Updates Moveable Locations
		self.__chessGame.updateTracking(pieceObject) ##Updates all used positions
		print(f"Next Moves: {pieceObject.canMoveHere}")

	def findNextMove(self, debugActive):
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

	def get_piece(self, team=None, tagOrTile=None):
		if tagOrTile in self.whitePieces or tagOrTile in self.blackPieces:
			if team == "white":
				return self.whitePieces[tagOrTile]
			elif team == "black":
				return self.blackPieces[tagOrTile]
			elif team == None:
				pass
			else:
				print(f"Incorrect Team: {team} \n\t ERROR@ placements.get_piece")
		elif tagOrTile in self.__chessGame.tileTitleList:
			# print(tagOrTile) 
			for key in self.whitePieces.keys():
				if self.whitePieces[key].locationID == tagOrTile:
					print(f"Found {self.whitePieces[key].pieceID}")
					return self.whitePieces[key] 
			for key in self.blackPieces.keys():
				if self.blackPieces[key].locationID == tagOrTile:
					print(f"Found {self.blackPieces[key].pieceID} at {tagOrTile}")
					return self.blackPieces[key] 
		else:
			print(f"Incorrect tagOrTile: {tagOrTile}")

	## 0=Rook, 1=KNIGHT, 2=BISHOP, 3=KING, 4=QUEEN, 5=PAWN
	def get_object(self, title):
		if title == self.__pieceList[0].pieceID: ##ROOK
			return ROOK(self.__chessGame)
		elif title == self.__pieceList[1].pieceID:
			return KNIGHT(self.__chessGame)
		elif title == self.__pieceList[2].pieceID:
			return BISHOP(self.__chessGame)
		elif title == self.__pieceList[3].pieceID:
			return KING(self.__chessGame)
		elif title == self.__pieceList[4].pieceID:
			return QUEEN(self.__chessGame)
		elif title == self.__pieceList[5].pieceID:
			return PAWN(self.__chessGame)
		else:
			print(f"Incorrect Piece Name: {title} \n")