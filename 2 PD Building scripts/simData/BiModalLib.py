# BiModalLib.py
#--------------------------------------------------------------------------
#************************************************************************
#   CIN2																*
#	Daniel Grajales														*
#	File: BiModalLib.py													*
#	Version: 04.14 (0.5)												*
#	Purpose: To build a library with most common used functions.		*
#	Functionas as: save to file, read from file, build structure.		*
#																		*
#	April 2014. Barcelona, Spain. 										*
#************************************************************************
#---------------------------------------------------------------------------
import math
import cmath
from string import *
from pdPythonLib import *
import os

class slab:
	#parameter definitions:
 def __init__(self):
    self.size = 1
    self.layerIdx = 1
    self.rix = 1

 def buildLayer(self,appClass,nameOfNode,layerIdx,sizeLayer,rixLayer):
 	g = appClass
 	self.size = sizeLayer
 	self.layerIdx = layerIdx
 	self.rix = rixLayer
 	
 	g.AddCmd(nameOfNode+".insertlayer("+str(layerIdx)+")")
 	g.AddCmd(nameOfNode+".layers["+str(layerIdx)+"].size="+str(sizeLayer))
 	g.AddCmd(nameOfNode+".layers["+str(layerIdx)+"].nr11="+str(rixLayer))
 	g.AddCmd(nameOfNode+".layers["+str(layerIdx)+"].nr22="+str(rixLayer))
 	g.AddCmd(nameOfNode+".layers["+str(layerIdx)+"].nr33="+str(rixLayer))
 	#g.Exec(nameOfNode+".findorcreateview()")

