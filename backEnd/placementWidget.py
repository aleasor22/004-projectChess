#Imports here
# import tkinter
from .Pieces import *


class placements():
	def __init__(self, canvas, chessClass, blankPieces):
		self.__chessGame = chessClass
		self.__render = canvas
		self.__pieceList = blankPieces
		self.whitePieces = {}
		self.blackPieces = {}
		
	

	def createPieces(self, pieceName, quantity, team):
		for pieceNum in range(quantity):
			tag = f"{pieceName}-{pieceNum}"
			if team == "white":
				self.whitePieces[tag] = self.returnClass(pieceName)
				self.whitePieces[tag].myID = tag
			elif team == "black":
				self.blackPieces[tag] = self.returnClass(pieceName)
				self.blackPieces[tag].myID = tag


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
					columnNumber += 1
				elif "1" in key:
					location = f"{self.__chessGame.columnTitle[altColumnNum]}{backRow}"
					teamDict[key].setup(self.__chessGame.get_nwCoord(location), team, location)
					altColumnNum -= 1
			else:
				location = f"{self.__chessGame.columnTitle[pawnCount]}{frontRow}"
				teamDict[f"PAWN-{pawnCount}"].setup(self.__chessGame.get_nwCoord(location), team, location)
				pawnCount += 1


	## 0=Rook, 1=KNIGHT, 2=BISHOP, 3=KING, 4=QUEEN, 5=PAWN
	def returnClass(self, title):
		if title == self.__pieceList[0].pieceID: ##ROOK
			return ROOK(self.__render)
		elif title == self.__pieceList[1].pieceID:
			return KNIGHT(self.__render)
		elif title == self.__pieceList[2].pieceID:
			return BISHOP(self.__render)
		elif title == self.__pieceList[3].pieceID:
			return KING(self.__render)
		elif title == self.__pieceList[4].pieceID:
			return QUEEN(self.__render)
		elif title == self.__pieceList[5].pieceID:
			return PAWN(self.__render)
		else:
			print(f"Incorrect Piece Name: {title} \n")