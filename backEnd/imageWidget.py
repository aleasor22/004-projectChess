##List of Imports
import os
import tkinter as tk
from PIL import ImageTk, Image


##Start of the Image Class
class imageWidget:
	def __init__(self, canvas):
		"""Canvas is the the base layer of my application"""
		self.__render = canvas #Only for this class

		##General Data for the child classses
		self._imagePIL = None
		self._imgSize = None
		self._imageTK = {}
		# self._myTag = []
	
	def createImage(self, fileLocation, tag):
		self._imagePIL = Image.open(str(fileLocation))
		self._imgSize = self._imagePIL.size
		self._imageTK[tag] = ImageTk.PhotoImage(self._imagePIL)
		# self._myTag.append(tag)


	def placeImage(self, x, y, tag):
		self.__render.create_image(x, y, tag=tag, image=self._imageTK[tag], anchor="nw")

	def changedMyTag(self, oldTag, newTag):
		#Save Value from original key
		old_imageTK = self._imageTK[oldTag]

		#Delete Key & Value from dictionary
		del self._imageTK[oldTag]
		##Delete original Piece
		if len(self.__render.find_withtag(oldTag)) != 0:
			self.__render.delete(self.__render.find_withtag(oldTag)[1])
		#add original Value back with new Key
		self._imageTK[newTag] = old_imageTK

	def get_imageTK_Dict(self, key=False):
		if key:
			return self._imageTK.keys()
		else:
			return self._imageTK
	
	def get_size(self):
		return self._imgSize
	

	# ##TODO: Determin if Needed/used. Then Remove later
	# def get_myTag(self): ## Returns entire List
	# 	return self._myTag