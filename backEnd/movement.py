import os
import tkinter
from .Pieces import SELECT


class Move():
	def __init__(self, chessObject, placements):
		self.__chess = chessObject
		self.__render = chessObject.get_canvas()
		self.__place = placements

		self.__select = SELECT(self.__render)
		self.__currPiece = None
				

	def selectPiece(self, mouseLocation):
		print(f"Mouse clicked at: {mouseLocation}")
		position = self.__chess.get_nwCoord(mouseLocation)
		self.__select.removeImage()
		self.__select.placeImage(position[0], position[1], mouseLocation)
		self.__currPiece = self.__place.get_piece(tagOrTile=mouseLocation) 
		return self.__currPiece
		

	def movePiece(self, mouseLocation):
		print(self.__currPiece, "OBJECT")
		self.__place.place(self.__currPiece, mouseLocation)
		