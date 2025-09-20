##List of  Imports
import os
from backEnd.imageWidget import imageWidget
from Images import *


##Start of Class PAWN
class BISHOP(imageWidget):
	def __init__(self, canvas):
		imageWidget.__init__(self, canvas)
		self.pieceID = "BISHOP"
		
		##List of Moves
		self.canMoveHere = []
		self.moveSet = set()
		

	def setup(self, pos, color, tag):
			self.set_team(color)
			self.createImage()
			self.placeImage(pos[0], pos[1], tag)

	def availableMoves(self):
		# print(f"{self.myTeam}-{self.myID}'s Moves are being calculated")
		##Resets List
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index = self._chessObject.MATRIX.findMatrixIndex(self.locationID)
		# print(f"Index= {index} & Location= {self.myGlobalMatrix[index[0]][index[1]]}")
		i = -1
		j = 0

		while i < 16:
			i += 1
			try:
				if i <= 7:
					if (index[0]+i) <=7:
						# print(f"i:{i}={self.myGlobalMatrix[index[0]+i][index[1]+i]}", end=" ")
						self.moveSet.add(self.myGlobalMatrix[index[0]+i][index[1]+i])
					if (index[0]-i) >= 0:
						# print(f"i:{i}={self.myGlobalMatrix[index[0]-i][index[1]+i]}", end=" ")
						self.moveSet.add(self.myGlobalMatrix[index[0]-i][index[1]+i])
				elif i > 7:
					if (index[0]+j) <= 7:
						# print(f"j:{j}={self.myGlobalMatrix[index[0]+j][index[1]-j]}", end=" ")
						self.moveSet.add(self.myGlobalMatrix[index[0]+j][index[1]-j])
					if (index[0]-j) >= 0:
						# print(f"j:{j}={self.myGlobalMatrix[index[0]-j][index[1]-j]}", end=" ")
						self.moveSet.add(self.myGlobalMatrix[index[0]-j][index[1]-j])
					j += 1
					
			except IndexError:
				# print(f"colummn: {index[0]+i}, row: {index[1]+i}", end=" | ")
				# print(f"colummn: {index[0]-i}, row: {index[1]+i}")
				continue
		
		print("Moves Calulated:", self.canMoveHere)
		self.setToList()
				
			

	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackBishop.png"
		elif color == "white":
			self._imgLocation = "Images/WhiteBishop.png"
		else:
			print("Incorrect team selected @Bishop.set_team()")