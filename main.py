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

from Dataset.dataset import FileHandler, Transformer

if __name__ == '__main__':
    
    value = {'Angle' : 0, 'Distance' : 1}
    
    fh = FileHandler()
    fh.generateDataSet()
    ds = fh.getDataSet
    
    