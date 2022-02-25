import pytest

from playground.classes.example import Something
from playground.data.datamod import DataClass

def testStuff(caplog):
	s=Something()
	dc=DataClass(100)
	z=s.do(dc.x,dc.y) # add x and y as vectors
	assert len(z) == 100 # just check the length
	z=s.dodc(dc) # use data class directly
	assert len(z) == len(dc.x)
