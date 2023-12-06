"""
    lidiaAcedrg_gui.py
    Copyright (C) 2015 Newcastle University
    Author: Martin Noble
    
    """

from PySide2 import QtGui, QtWidgets,QtCore

from qtgui.CCP4TaskWidget import CTaskWidget

#-------------------------------------------------------------------
class lidiaAcedrg_gui(CTaskWidget):
    #-------------------------------------------------------------------
    TASKMODULE = 'test'       # Where this plugin will appear on the gui
    TASKTITLE = 'MAKE LIGAND'     # A short title for gui menu
    DESCRIPTION = 'Generate a PDB file and dictionary (acedrg) from MOL file, SMILES, or sketch (lidia)'
    TASKVERSION = 0.1
    TASKNAME = 'LidiaAcedrg'
    RANK=1

    def drawContents(self):
        
        self.openFolder(folderFunction='inputData')
        
        self.createLine ( [ 'advice',' '] )
        self.createLine ( [ 'advice',' '] )
        
        self.createLine(['subtitle','Start point'])
        self.openSubFrame( frame=[True])
        self.createLine ( [ 'label','Start with molecular structure from ','stretch','widget','MOLSMILESORSKETCH' ] )
        
        self.createLine ( [ 'advice', 'Will launch Lidia to sketch molecule. Click Apply <b>and</b> Close in Lidia when sketch is ready.' ], toggle=['MOLSMILESORSKETCH','open',['SKETCH']])
        self.createLine ( [ 'advice', 'Optionally can provide a starting monomer for the Lidia sketch:' ], toggle=['MOLSMILESORSKETCH','open',['SKETCH']])
        
        self.createLine ( [ 'widget','MOLIN' ], toggle=['MOLSMILESORSKETCH','open',['SKETCH','MOL']] )
        
        self.createLine ( [ 'label', 'SMILES string', 'widget', '-guiMode', 'multiLine', 'SMILESIN' ] , toggle=['MOLSMILESORSKETCH','open',['SMILES']])
        self.closeSubFrame()


        self.createLine(['subtitle','Output monomer'])
        self.openSubFrame( frame=[True])
        self.createLine ( [ 'label','Three letter code for output monomer','stretch','widget','TLC' ] )
        self.closeSubFrame()
        
        self.openFolder(title='Advanced')
        self.createLine(['advice','Geometry restraints *always* taken from ACEDRG'])
        self.createLine(['label','Output conformers generated by','stretch','widget','CONFORMERSFROM'])
        self.openSubFrame( frame=[False], toggle=['CONFORMERSFROM','open',['RDKIT']] )
        self.createLine ( [ 'label','Number of random RDKit start structures','widget','-toolTip','More start structures may provide a beter start conformer','NRANDOM' ] )
        self.closeSubFrame()




    def isValid(self):
        invalidElements = super(lidiaAcedrg_gui, self).isValid()
        if self.container.inputData.MOLSMILESORSKETCH.__str__() == 'SMILES':
            self.container.inputData.MOLIN.unSet()
        return invalidElements
