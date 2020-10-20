'''
Created on Oct 17, 2020

@author: thek1d
'''
import math
from   tkinter           import filedialog
import pandas            as     pd
import platform          as     pt
import matplotlib.pyplot as     plt


class FileHandler():
    
    def __init__(self):
        self._filename = ""
        self._dataSet = {}                              #rowwise data as dictionary -> key : index of data
        self._dataSetDict = {}                          #dictionary which includes reference to data dictionary (key : Name of Scan)
        
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

                                    
    def generateDataSet( self ):
        sheet_names = pd.ExcelFile(self._filename).sheet_names
                
        for num_sheet in range(len(sheet_names)):
            sheet = pd.read_excel(self._filename, sheet_name=sheet_names[num_sheet], header=None)
            for row in range(len(sheet)):
                ''' making dictionary for Scan's {n-th entry : [Angle, Distance]} '''
                self._dataSet.update({row : [ sheet.iloc[row][0], sheet.iloc[row][1] ]})
                
            temp = self._dataSet.copy()
            ''' linking Scan's to entries -> dataSetDict = { Scan1 : {0 : [a0, d0]}, {1 : [a1, d1]}, ... } '''    
            self._dataSetDict.update({sheet_names[num_sheet] : temp})
            
        return self._dataSetDict
            
class Transformer():
    
    def __init__(self):
        self._x = 0
        self._y = 0
        self._dataSetRobotCoordinates = {}
        self._dataSetWorldCoordinates = {}
    
    def calculateRobotCoordinates(self, scan):
        value = {'Angle' : 0, 'Distance' : 1}
        for row in range(len(scan)):
            self._x = scan[row][value['Distance']] * math.cos(math.radians(scan[row][value['Angle']]))
            self._y = scan[row][value['Distance']] * math.sin(math.radians(scan[row][value['Angle']]))
            self._dataSetRobotCoordinates.update({row : [self._x, self._y]})
            
        temp = self._dataSetRobotCoordinates.copy()
        return temp
    
    def calculateWorldCoordinates(self, rcScan, posOrigToRobScan):
        value = {'x' : 0, 'y' : 1, 'Angle' : 2}
        for row in range(len(rcScan)):
            
            self._x =( posOrigToRobScan['x'] + 
            math.cos(posOrigToRobScan['Angle']) * rcScan[row][value['x']] - 
            math.sin(posOrigToRobScan['Angle']) * rcScan[row][value['y']] )
            
            self._y =( posOrigToRobScan['y'] + 
            math.sin(posOrigToRobScan['Angle']) * rcScan[row][value['x']] + 
            math.cos(posOrigToRobScan['Angle']) * rcScan[row][value['y']] )
            
            self._dataSetWorldCoordinates.update({row : [self._x, self._y]})
        
        temp = self._dataSetWorldCoordinates.copy()    
        return temp  
        
class Plotter():
    
    def __init__(self):
        pass
    
    def plot(self, wcScan1, wcScan2, wcScan3):
        value = {'x' : 0, 'y' : 1}
        for row in range(len(wcScan1)):
            plt.plot(wcScan1[row][value['x']], wcScan1[row][value['y']], 'ro',
                     wcScan2[row][value['x']], wcScan2[row][value['y']], 'bo',
                     wcScan3[row][value['x']], wcScan3[row][value['y']], 'go')
        plt.grid(True)
        plt.show()
        
                    