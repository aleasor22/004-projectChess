##Imports
from ..imageWidget import imageWidget
from Images import *

class SELECT(imageWidget):
	def __init__(self, canvas):
		super().__init__(canvas)
		self._imgLocation = "Images/SelectedPiece.png"
		self.pieceID = "SELECTED"

		self.createImage()


	# def setup(self, ):
	# 	self.