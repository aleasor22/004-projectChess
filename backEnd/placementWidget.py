#Imports here
# import tkinter
from .Pieces import *


class placements():
	def __init__(self, canvas, chessClass):
		self.__chessGame = chessClass
		self.__render = canvas
		self.whitePieces = [ROOK(canvas), KNIGHT(canvas), BISHOP(canvas), KING(canvas), QUEEN(canvas), PAWN(canvas)]
		self.blackPieces = [ROOK(canvas), KNIGHT(canvas), BISHOP(canvas), KING(canvas), QUEEN(canvas), PAWN(canvas)]
		
	
	def placeTeamWhite(self, ):
		##ROOK Setups
		self.whitePieces[0].rookSetup(self.__chessGame.get_nwCoord("a1"), "white", "a1")
		self.whitePieces[0].rookSetup(self.__chessGame.get_nwCoord("h1"), "white", "h1")
		
		##KNIGHT Setups
		self.whitePieces[1].knightSetup(self.__chessGame.get_nwCoord("b1"), "white", "b1")
		self.whitePieces[1].knightSetup(self.__chessGame.get_nwCoord("g1"), "white", "g1")

		##BISHOP Setups
		self.whitePieces[2].bishopSetup(self.__chessGame.get_nwCoord("c1"), "white", "c1")
		self.whitePieces[2].bishopSetup(self.__chessGame.get_nwCoord("f1"), "white", "f1")
		
		##KING/QUEEN Setups
		self.whitePieces[3].kingSetup(self.__chessGame.get_nwCoord("d1"), "white", "d1")
		self.whitePieces[4].queenSetup(self.__chessGame.get_nwCoord("e1"), "white", "e1")

		##PAWN Setups
		for column in self.__chessGame.rowTitle:
			self.whitePieces[5].pawnSetup(self.__chessGame.get_nwCoord(column+"2"), "white", column+"2")
			

	def placeTeamBlack(self, ):
		##ROOK Setups
		self.blackPieces[0].rookSetup(self.__chessGame.get_nwCoord("a8"), "black", "a8")
		self.blackPieces[0].rookSetup(self.__chessGame.get_nwCoord("h8"), "black", "h8")
		
		##KNIGHT Setups
		self.blackPieces[1].knightSetup(self.__chessGame.get_nwCoord("b8"), "black", "b8")
		self.blackPieces[1].knightSetup(self.__chessGame.get_nwCoord("g8"), "black", "g8")

		##BISHOP Setups
		self.blackPieces[2].bishopSetup(self.__chessGame.get_nwCoord("c8"), "black", "c8")
		self.blackPieces[2].bishopSetup(self.__chessGame.get_nwCoord("f8"), "black", "f8")
		
		##KING/QUEEN Setups
		self.blackPieces[3].kingSetup(self.__chessGame.get_nwCoord("d8"), "black", "d8")
		self.blackPieces[4].queenSetup(self.__chessGame.get_nwCoord("e8"), "black", "e8")

		##PAWN Setups
		for column in self.__chessGame.rowTitle:
			self.blackPieces[5].pawnSetup(self.__chessGame.get_nwCoord(column+"7"), "black", column+"7")

