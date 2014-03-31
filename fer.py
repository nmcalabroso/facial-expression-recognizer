from __future__ import division
import time
from fann_analyze_image import classifier

#Facial Expression Recognizer
class FER():
	def __init__(self):
		self.classifier = classifier()
		
	def predict(self,input):
		out = self.classifier.analyze(input)
		if out == True:
			return 1
		return 0