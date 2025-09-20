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


	def availableMoves(self):
		# print(f"{self.myTeam}-{self.myID} Moves are being calculated")
		##New Call Resets
		currRow = self.locationID[1]
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index_A, index_B = self._chessObject.MATRIX.findMatrixIndex(self.locationID)

		if "White" in self._imgLocation:
			for col in range(-1, 2):
				try:
					if index_A+col < 0:
						raise IndexError
					self.moveSet.add(self.myGlobalMatrix[index_A+col][index_B+1])
					if col == 0 and currRow == "2":
						# print(self.myGlobalMatrix[index_A+col][index_B+2])
						self.moveSet.add(self.myGlobalMatrix[index_A+col][index_B+2])
				except IndexError:
					continue
		if "Black" in self._imgLocation:
			for col in range(-1, 2):
				try:
					if index_A+col < 0:
						raise IndexError
					self.moveSet.add(self.myGlobalMatrix[index_A+col][index_B-1])
					if col == 0 and currRow == "7":
						# print(self.myGlobalMatrix[index_A+col][index_B-2])
						self.moveSet.add(self.myGlobalMatrix[index_A+col][index_B-2])
				except IndexError:
					continue	
		self.setToList()
		# print("Moves Calculated:", self.canMoveHere)

	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackPawn.png"
		elif color == "white":
			self._imgLocation = "Images/WhitePawn.png"
		else:
			print("Incorrect team selected @PAWN.set_team()")
