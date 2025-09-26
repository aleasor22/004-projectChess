import os
import tkinter
from .Pieces import SELECT


class Move():
	def __init__(self, chessObject, placeObject):
		self.__chess = chessObject
		self.__render = chessObject.get_canvas()
		self.__place = placeObject

		self.__select = SELECT(chessObject)
		self.__currPiece = None
		self.__originLoc = None

		self.noActivePrompt = True
				

	def selectPiece(self, mouseLocation):
		print(f"Mouse clicked at: {mouseLocation}")
		self.__originLoc = mouseLocation
		position = self.__chess.get_nwCoord(mouseLocation)
		self.__select.removeImage()
		self.__select.placeImage(position[0], position[1], mouseLocation)
		self.__currPiece = self.__place.get_piece(tagOrLocation=mouseLocation) 
		if self.__currPiece != None:
			self.__currPiece.availableMoves()
			print(f"Piece: {self.__currPiece.myID}, Can Move Here: {self.__currPiece.canMoveHere}")
		return self.__currPiece
		

	def movePiece(self, mouseLocation):
		self.__place.place(self.__currPiece, mouseLocation)
		self.__chess.MATRIX.updatePieceMatrix(self.__originLoc, mouseLocation)
		# self.__place.findNextMove()

	def get_piece(self, pieceAtLocation):
		return self.__place.get_piece(pieceAtLocation)
	
	def isLocationTaken(self, underPiece):
		return self.__place.isOpponent(self.__currPiece, underPiece)
	


	## Used to Force Move by Terminal Inputs
	##NOTE: Scrapping this idea till further notice
	##		Will need to have a list of move IDs, to know which piece moves where, and how. 
	##		EX: Qf5 or KNxd3 or e5 known as a pawn move
	def forceMove(self, ):
		userIn = str(input("Make Your Move \n\t>>"))

		if self.__chess.MATRIX.foundInMatrix(userIn):
			# index_A, index_B = self.__chess.MATRIX.findMatrixIndex(userIn)
			# posX, posY = self.__chess.get_nwCoord(userIn)
			self.__place.place(self.__place.get_piece(userIn), userIn)

		else:
			print("Not a move - Try Again")