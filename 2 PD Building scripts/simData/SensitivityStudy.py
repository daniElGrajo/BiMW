# SensitivityStudy.py
#--------------------------------------------------------------------------
#************************************************************************
#   CIN2																*
#	Daniel Grajales														*
#	File: SensitivityStudy.py													*
#	Version: 04.14 (0.5)												*
#	Purpose: as first approach it would be convenient to explore		*
#	the effective index in SM and BiModal areas as experinced by		*
#	the two fundamental modes, in both TE and TM polarizations. 		*
#	Objective: To save the EffRIX into a file. Start with TE. 			*
#	Then TM, and finally make it as a automatic sweep (in a for loop). 	*
#																		*
#	April 2014. Barcelona, Spain. 										*
#************************************************************************
#---------------------------------------------------------------------------

# import libraries. Specially Photon Design Library.
# from string import *
# from cmath import *
# from array import *
# from pdPythonlib import *
from string import *
import sys
from pdPythonLib import *
from BiModalLib import *
# make my own library with methods as: save to file, read from file, etc.
# Build my SCT file as required.

# Connect to APP

f = pdApp()
f.ConnectToApp()
# Add connection lock to ensure how to handle errors and exceptions

# DGG april 2014 TODO: make a script parser to read SCT files and parse them into PD sim


# start a new project
# partial mode
#f.AddCmd("app.closeall()")

f.AddCmd("app.addsubnode(fimmwave_prj,BiModalWG)")
# Return a reference and keep it in scriptMain
scriptMain = "app.subnodes[1]"

# now build a bimodalSection with SA
# f.Exec(scriptMain+".addsubnode(slabwgNode,BiModalSaWG)")
# BiMSaSlabNodeStr = "app.subnodes[1].subnodes[1]"
# BiModalSaSlab = slab()
# BiModalSaSlab.buildLayer(f,BiMSaSlabNodeStr,1,	2.0,		1.46)
# BiModalSaSlab.buildLayer(f,BiMSaSlabNodeStr,2,	0.34,	2.00)
# BiModalSaSlab.buildLayer(f,BiMSaSlabNodeStr,3,	1.5,	1.33)
# # Finished building bimodal with SA WG ***************************************************

# # start building a singleMode WG ************************************************************
# f.Exec(scriptMain+".addsubnode(slabwgNode,SingleModeWG)")
# SingleModeSlabNodeStr = "app.subnodes[1].subnodes[2]"
# # start by making a slab object and create 3 layers as required
# # buildLayer(self, appClass, nameOfNode, layerIdx, sizeLayer, rixlayer)
# singleModeSlab = slab()
# singleModeSlab.buildLayer(f,SingleModeSlabNodeStr,1,	2.0,		1.46)
# singleModeSlab.buildLayer(f,SingleModeSlabNodeStr,2,	0.15,	2.00)
# singleModeSlab.buildLayer(f,SingleModeSlabNodeStr,3,	1.69,	1.46)
# Finished building single mode WG ***********************************************************

# now build a bimodalSection
f.Exec(scriptMain+".addsubnode(slabwgNode,BiModalWG)")
BiModalSlabNodeStr = "app.subnodes[1].subnodes[3]"
BiModalSlab = slab()
BiModalSlab.buildLayer(f,BiModalSlabNodeStr,1,	2.0,	1.46)
BiModalSlab.buildLayer(f,BiModalSlabNodeStr,2,	0.34,	2.00)
BiModalSlab.buildLayer(f,BiModalSlabNodeStr,3,	1.5,	1.46)
f.Exec(BiModalSlabNodeStr+".findorcreateview()")
# Finished building bimodal  WG ***********************************************************


del f

