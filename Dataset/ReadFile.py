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
        self._dataset = []
        
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
        else: 
            self._filename = filedialog.askopenfilename( initialdir="/User",
                                                         title="Open File",
                                                         filetypes=(("Excel Files", ".xlsx .xls"),("All Files", "*.*")) )

    '''Generating dataframe from Excel sheet'''                                
    def getDataSet( self ):              
        scan_ds = {}
        offset = 0
        row = 0
        
        sheets_names = pd.ExcelFile(self._filename).sheet_names
        
        for num_sheet in range(len(sheets_names)):
            sheet = pd.read_excel(self._filename, sheet_name=sheets_names[num_sheet], header=None)
            offset = num_sheet * (row + 1)
            for row in range(len(sheet)):
                scan_ds.update({row + offset : [ sheet.iloc[row][0], sheet.iloc[row][1] ]})
                    
        return scan_ds
        
        
            
    
    


        