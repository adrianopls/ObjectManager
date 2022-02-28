# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:17:09 2022

@author: Adriano
"""


from .density import Density



class Image(Density):
    tid = "image"
    _TID_FRIENDLY_NAME = "Image"

    
    _SHOWN_ATTRIBUTES = [("width", "Width"),
                          ("height", "Height")
    ]

    def __init__(self, data, **attributes):
        super().__init__(data, **attributes)
    
    @property
    def width(self):
        if self._data is None:
            return None
        #return self._data.shape[-1]
        return self._data.shape[1]
        
    @property
    def height(self):
        if self._data is None:
            return None
        #return self._data.shape[-2]   
        return self._data.shape[0]
    

            
        
    
    
