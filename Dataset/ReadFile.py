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
                
    @property        
    def getSheetNames(self):
        sheets_names = pd.ExcelFile(self._filename).sheet_names
        return sheets_names
        
        '''for i in range(len(sheets_names)):
            df = pd.DataFrame()'''
        #return pd.read_excel(self._filename, sheet_name="Scan 1")
    
    


        