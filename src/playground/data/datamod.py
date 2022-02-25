import numpy as np

class DataClass:
	def __init__(self,n=10):
		self.x=np.array([np.random.rand() for i in range(n)])
		self.y=np.array([np.random.rand() for i in range(n)])
		return
	def Thing(self):
		print('la')
