'''
Created on Oct 17, 2020

@author: thek1d
'''

'''
print(ds['Scan1'])                           -> prints whole DataSet Scan1
print(ds['Scan1'][0])                        -> prints first entry of Scan1 (Angle & Distance)
print(ds['Scan3'][1][value['Distance']])     -> prints Distance from the second entry of Scan3
print(ds['Scan2'][3][value['Angle']])        -> prints Angle from the fourth entry of Scan2
'''

from Dataset.dataset import FileHandler, Transformer, Plotter
import math

if __name__ == '__main__':
    
    fh = FileHandler()
    ds = fh.generateDataSet()
    
    tf = Transformer()
    rcScan1 = tf.calculateRobotCoordinates(ds['Scan1'])
    rcScan2 = tf.calculateRobotCoordinates(ds['Scan2'])
    rcScan3 = tf.calculateRobotCoordinates(ds['Scan3'])
    
    ''' Origin coordinates, shift vector '''
    cordinatesOrigin2RobotScan1 = {'x' : 10, 'y' : 30, 'Angle' : math.radians(45)}
    cordinatesOrigin2RobotScan2 = {'x' : 50, 'y' : 50, 'Angle' : math.radians(120)}
    cordinatesOrigin2RobotScan3 = {'x' : 90, 'y' : 40, 'Angle' : math.radians(-17)}
    
    wcScan1 = tf.calculateWorldCoordinates(rcScan1, cordinatesOrigin2RobotScan1)
    wcScan2 = tf.calculateWorldCoordinates(rcScan2, cordinatesOrigin2RobotScan2)
    wcScan3 = tf.calculateWorldCoordinates(rcScan3, cordinatesOrigin2RobotScan3)
            
    pt = Plotter()
    pt.plotAllData(wcScan1, wcScan2, wcScan3)
    

    
        
    
    