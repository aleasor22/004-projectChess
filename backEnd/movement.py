import os
import tkinter
from .imageWidget import imageWidget


class Move(imageWidget):
	def __init__(self, canvas):
		imageWidget.__init__(self, canvas)
		
		

	def selectPiece(self, ):
		pass

	def movePiece(self, oldTag, newTag, newPos):
		self.changedMyTag(oldTag, newTag)
		self.placeImage(newPos[0], newPos[1], newTag)


	def set_position(self, spot):
		self.tablePosition = spot
		pass
	