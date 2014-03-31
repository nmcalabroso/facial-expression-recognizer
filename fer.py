from __future__ import division
import time
from fann_analyze_image import classifier

#Facial Expression Recognizer
class FER():
	def __init__(self):
		self.classifier = classifier()
		
	def predict(self,input):
		output = self.classifier.analyze(input)
		if output == True:
			return 1
		return 0 #temporary