'''
Created on Oct 17, 2020

@author: thek1d
'''

from tkinter import filedialog
import pandas as pd
import platform as pt

class FileHandler():
    
    def __init__(self):
        self._filename = ""
        self._dataSet = {}                              #rowwise data as dictionary -> key : Scanx
        self._dataSetDict = {}                          #dictionary which includes reference to data dictionary
        
        self.__getFileName()
    
    
    def __getFileName(self):
        if pt.system() == "Linux":
            self._filename = filedialog.askopenfilename( initialdir="/home/thek1d/Privat/FHV/Kurse/1_Semester/Autonome_Systeme_Bewegung/Occupancy_Grid_Map",
                                                         title="Open File",
                                                         filetypes=(("Excel Files", ".xlsx .xls"),("All Files", "*.*")) )
        elif pt.system() == "Windows":
            self._filename = filedialog.askopenfilename( initialdir="C:/",
                                                         title="Open File",
                                                         filetypes=(("Excel Files", ".xlsx .xls"),("All Files", "*.*")) )
        #Unix
        else: 
            self._filename = filedialog.askopenfilename( initialdir="/User",
                                                         title="Open File",
                                                         filetypes=(("Excel Files", ".xlsx .xls"),("All Files", "*.*")) )

    '''Generating dataframe from Excel sheet'''                                
    def generateDataSet( self ):
        sheet_names = pd.ExcelFile(self._filename).sheet_names
        
        for num_sheet in range(len(sheet_names)):
            sheet = pd.read_excel(self._filename, sheet_name=sheet_names[num_sheet], header=None)
            for row in range(len(sheet)):
                ''' making dictionary for Scan's {n-th entry : [Angle, Distance]} '''
                self._dataSet.update({row : [ sheet.iloc[row][0], sheet.iloc[row][1] ]})
            ''' linking Scan's to entries -> dataSetDict = { Scan1 : {0 : [a0, d0]}, {1 : [a1, d1]}, ... }'''    
            self._dataSetDict.update({sheet_names[num_sheet] : self._dataSet})
    
    @property
    def getDataSet(self):
        return self._dataSetDict
            
class Transformer():
    
    def __init__(self):
        pass
    
            
        
            
    
    


        