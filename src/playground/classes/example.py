import os
import sys
import numpy as np
from playground.data.datamod import *

class Something:
	def __init__(self):
		print('init')
	def do(self,x,y):
		return(x+y)
	def dodc(self,dc):
		return(dc.x+dc.y)
