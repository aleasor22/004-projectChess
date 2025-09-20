##List of  Imports
import os
from backEnd.imageWidget import imageWidget
from Images import *


##Start of Class PAWN
class KNIGHT(imageWidget):
	def __init__(self, canvas):
		imageWidget.__init__(self, canvas)
		self.pieceID = "KNIGHT"
		
		##List of Moves
		self.canMoveHere = []


	def setup(self, pos, color, tag):
			self.set_team(color)
			self.createImage()
			self.placeImage(pos[0], pos[1], tag)

	def availableMoves(self, ):
		# print(f"{self.myTeam}-{self.myID}'s Moves are being calculated")
		##Resets
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index_A, index_B = self._chessObject.MATRIX.findMatrixIndex(self.locationID)

		for i in range(-2, 3):
			for j in range(-2, 3):
				try:
					if index_A+j < 0 or index_B+i < 0:
						raise IndexError
					if j % 2 == 0 and (i == -2 or i == 2):
						raise IndexError
					elif (i==-1 or i==1) and (j>=-1 and j<=1):
						raise IndexError
					elif (i==0 and j!=0):
						raise IndexError
					else:
						# print(self.myGlobalMatrix[index_A+j][index_B+i], end=" ")
						self.moveSet.add(self.myGlobalMatrix[index_A+j][index_B+i])
				except IndexError:
					# print("**", end=" ")
					continue
			# print()

		# print("Moves Calculated:", self.canMoveHere)
		self.setToList()
				


	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackKnight.png"
		elif color == "white":
			self._imgLocation = "Images/WhiteKnight.png"
		else:
			print("Incorrect team selected @Knight.set_team()")