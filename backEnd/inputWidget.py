from .imageWidget import imageWidget
from pynput import keyboard
from Images import * #imports Image file locations
import pygetwindow

import tkinter ##Used for Debugging

class Inputs():
	def __init__(self, chessObject, place):
		self.__listeningStarted =  False ##Is this needed
		self.__chessGame = chessObject
		self.__render = chessObject.get_canvas()
		self.__place = place
		
		self.applicationActive = False
		self.currMouseLocation = None
		self.oldMouseLocation = None
		self.clickCount = 0
		
		self.__listenForKeyboard = keyboard.Listener(on_press=self.onPress, on_release=self.onRelease)
		
		##Starts listening for keyboard & mouse events
		self.__listenForKeyboard.start()


	##Logic for Mouse Inputs##
	def bindEvents(self):
		if self.applicationActive:
			self.__render.bind("<Motion>", self.findMyMouse)
			self.__render.bind("<Button-1>", self.onMousePress)
		else:
			self.__render.unbind("<Motion>")
			self.__render.unbind("<Button-1>")

	##Below method got moved to placementWidget.py
	def onMousePress(self, event):
		if self.clickCount == 0:
			self.__place.selectPiece(self.currMouseLocation)
			if self.__place.activePiece:
				self.clickCount += 1

		elif self.clickCount == 1:
			self.__place.movePiece(self.currMouseLocation, True)
			self.clickCount = 0

	def findMyMouse(self, event):
		try: 
			matchingCanvasIDs = None
			for bbox in self.__chessGame.bboxTileList:
				if event.x > bbox[0] and event.x < bbox[2]:
					if event.y > bbox[1] and event.y < bbox[3]:
						matchingCanvasIDs = self.__render.find_overlapping(bbox[0]+1, bbox[1]+1, bbox[2]-1, bbox[3]-1)[0]
						break

			self.currMouseLocation = self.__render.gettags(matchingCanvasIDs)[0] ##Saves current mouse location
			if self.currMouseLocation != self.oldMouseLocation:
				self.oldMouseLocation = self.currMouseLocation ##Saves original Mouse location

				
			if self.__place.activePiece:
				self.__place.movePiece(self.currMouseLocation)

		except tkinter.TclError as error:
			##currently triggers when perfectly inbetween tiles
			# print(f"Caught Error: {error} \n\t Error@ inputs.findMyMouse")
			pass

	##Logic for Keyboard inputs##
	def onPress(self, key):
		# try:
		# 	print('alphanumeric key {0} pressed'.format(key.char))
		# except AttributeError:
		# 	print('special key {0} pressed'.format(key))
		pass

	##Logic to Track Keyboard Inputs
	def onRelease(self, key):
		try:
			print(f'alphanumeric key {key.char} released')
		except AttributeError:
			##Kills program when the "escape" key is pressed
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
		except AttributeError as error:
			print(f"Caught Error: {error} \n\t @get_activeWindowTitle()")