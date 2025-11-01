from ..imageWidget import IMAGE
from Images import *

class PIECES(IMAGE):
	def __init__(self, chess):
		IMAGE.__init__(self, chess)
		self._chess = chess

		##Point System
		self.piecePoints = 0

		##Movement Logic
		self.moveSet = set()
		self.hasMoved = False
		self.isPinned = False
		self.pinnedMoves = []
		
		##Visual aspect of Movement Logic
		self._shownMoves = [] ##Holds canvas IDs of a pieces possible moves
		self._showMovesImg = IMAGE(chess)
		self._showMovesImg.createImage("Images/possibleMove.png")

	
	def showMyMoves(self):
		self._shownMoves = [] ##Resets List
		if len(self.moveSet) > 0:
			for location in self.moveSet:
				self._showMovesImg.placeImage(location)
				self._shownMoves.append(self._showMovesImg.canvasID)
			# print(self._shownMoves)
	
	def delShownMoves(self):
		for id in self._shownMoves:
			self._render.delete(id)

	def isInList(self, ID, myList):
		if ID in myList:
			return True
		return False