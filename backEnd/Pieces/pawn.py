##List of  Imports
import os
from backEnd.imageWidget import imageWidget
from Images import *


##Start of Class PAWN
class PAWN(imageWidget):
	def __init__(self, canvas):
		imageWidget.__init__(self, canvas)
		self.pieceID = "PAWN"
		
		##List of Moves
		self.canMoveHere = []

	def setup(self, pos, color, tag):
		self.set_team(color)
		self.createImage()
		self.placeImage(pos[0], pos[1], tag)


	def availableMoves(self, ):
		##New Call Recets
		currColumn = self.locationID[0]
		currRow = self.locationID[1]
		self.canMoveHere = []

		
		##Logic for diagonal spaces
		currColumnIndex = -1
		for index in range(len(self._chessObject.columnTitle)):
			if currColumn == self._chessObject.columnTitle[index]:
				currColumnIndex = index
				break
			
		##White Piece Logic
		if "White" in self._imgLocation:
			try:
				if currColumnIndex-1 < 0:
					raise IndexError(f"Index out of range {currColumnIndex-1}")
				self.canMoveHere.append(f"{self._chessObject.columnTitle[currColumnIndex-1]}{int(currRow)+1}")
			except IndexError as outOfRange:
				# print(outOfRange)
				pass
			self.canMoveHere.append(f"{currColumn}{int(currRow)+1}")
			try:
				self.canMoveHere.append(f"{self._chessObject.columnTitle[currColumnIndex+1]}{int(currRow)+1}")
			except IndexError as outOfRange:
				# print(outOfRange)
				pass
			if currRow == "2":
				self.canMoveHere.append(f"{currColumn}{int(currRow)+2}")

		##Black Piece Logic
		elif "Black" in self._imgLocation:
			try:
				if currColumnIndex-1 < 0:
					raise IndexError(f"Index out of range {currColumnIndex-1}")
				self.canMoveHere.append(f"{self._chessObject.columnTitle[currColumnIndex-1]}{int(currRow)-1}")
			except IndexError as outOfRange:
				# print(outOfRange)
				pass
			self.canMoveHere.append(f"{currColumn}{int(currRow)-1}")
			try:
				self.canMoveHere.append(f"{self._chessObject.columnTitle[currColumnIndex+1]}{int(currRow)-1}")
			except IndexError as outOfRange:
				# print(outOfRange)
				pass
			if currRow == "7":
				self.canMoveHere.append(f"{currColumn}{int(currRow)-2}")
		
			

	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackPawn.png"
		elif color == "white":
			self._imgLocation = "Images/WhitePawn.png"
		else:
			print("Incorrect team selected @PAWN.set_team()")
