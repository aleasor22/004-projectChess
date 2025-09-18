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
				

	def selectPiece(self, mouseLocation):
		print(f"Mouse clicked at: {mouseLocation}")
		position = self.__chess.get_nwCoord(mouseLocation)
		self.__chess.set_origin(mouseLocation)
		self.__select.removeImage()
		self.__select.placeImage(position[0], position[1], mouseLocation)
		self.__currPiece = self.__place.get_piece(tagOrLocation=mouseLocation) 
		return self.__currPiece
		

	def movePiece(self, mouseLocation):
		self.__place.place(self.__currPiece, mouseLocation)

