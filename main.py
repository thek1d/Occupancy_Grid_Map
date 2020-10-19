'''
Created on Oct 17, 2020

@author: thek1d
'''

from Dataset.ReadFile import FileHandler

if __name__ == '__main__':
    
    fh = FileHandler()
    ds = fh.getSheetNames
    print(ds)
    