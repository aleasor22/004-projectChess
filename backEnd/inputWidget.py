from .imageWidget import imageWidget
from pynput import keyboard
from Images import * #imports Image file locations
import pygetwindow

import tkinter
import sys
import traceback

class Inputs():
	def __init__(self, canvas, chessClass):
		self.__listeningStarted =  False
		self.__chessGame = chessClass
		self.__render = canvas
		
		self.applicationActive = False
		self.mouseLocation = None
		
		self.__listenForKeyboard = keyboard.Listener(on_press=self.onPress, on_release=self.onRelease)
		
		##Starts listening for keyboard & mouse events
		self.__listenForKeyboard.start()


	##Logic for Mouse Inputs##
	def bindEvents(self, ):
		if self.applicationActive:
			self.__render.bind("<Motion>", self.findMyMouse)
			# self.__render.bind("<Button-1>", self.onMousePress)
		else:
			self.__render.unbind("<Motion>")

	# def onMousePress(self, event):
	# 	if "default" in self.selectedPiece.get_imageTK_Dict(True):
	# 		self.selectedPiece.changedMyTag("default", self.mouseLocation)
	# 		self.selectedPiece.placeImage(self.__chessGame.get_nwCoords(self.mouseLocation), self.mouseLocation)
	# 	else:
	# 		self.selectedPiece.changedMyTag(self.selectedPiece.get_imageTK_Dict(True), self.mouseLocation)
	# 		self.selectedPiece.placeImage(self.__chessGame.get_nwCoords(self.mouseLocation), self.mouseLocation)

	# 	pass

	def findMyMouse(self, event):
		# print(event.x, event.y)
		try: 
			matchingCanvasIDs = None
			for bbox in self.__chessGame.bboxTileList:
				if event.x > bbox[0] and event.x < bbox[2]:
					if event.y > bbox[1] and event.y < bbox[3]:
						matchingCanvasIDs = self.__render.find_overlapping(bbox[0]+1, bbox[1]+1, bbox[2]-1, bbox[3]-1)[0]
						break
			
			
			self.mouseLocation = self.__render.gettags(matchingCanvasIDs)[0]
			# print(self.mouseLocation, " + ", matchingCanvasIDs)
		except tkinter.TclError:
			##currently triggers when perfectly inbetween tiles
			print("Variable 'matchingCanvasIDs' cannot be of NoneType")

	##Logic for Keyboard inputs##
	def onPress(self, key):
		pass
		# try:
		# 	print('alphanumeric key {0} pressed'.format(key.char))
		# except AttributeError:
		# 	print('special key {0} pressed'.format(key))

	def onRelease(self, key):
		##kills program based on this if statement
		try:
			
			if key.char == 'q':
				# Stop listener
				self.stopListening()
				# self.unBindAllEvents() ##NOTE: May be needed later
				self.__render.quit()
			# print('alphanumeric key {} released'.format(key.char))
				# return False
		except AttributeError:
			if key == keyboard.Key.esc:
				self.stopListening()
				# self.unBindAllEvents() ##NOTE: May be needed later
				self.__render.quit()
			# print('special key {0} released'.format(key))
	
	def stopListening(self):
		self.__listeningStarted = False ##Sets listeningStarted to False
		##Stops the threads
		self.__listenForKeyboard.stop()


	
	##-------GETTERS/SETTERS-------##
	def get_activeWindowTitle(self):
		try:
			# print(pygetwindow.getActiveWindow().title)
			return pygetwindow.getActiveWindow().title
		except AttributeError:
			print("Window Can't be of NoneType")