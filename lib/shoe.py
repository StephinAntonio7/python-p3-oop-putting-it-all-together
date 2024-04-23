#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand:str, size):
        self.brand = brand
        self._size = size
        # self.repair = repair
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size (self, value):
        if value != int:
            print ("size must be an integer")
        else:
            self._size =value
    
    def cobble(self):
        self.condition = "New"
        print ("Your shoe is as good as new!")
    
            
    # def repair(self):
    #     return ("shoe has been repaired")
        
    pass