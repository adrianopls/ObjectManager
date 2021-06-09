
from collections import OrderedDict

from .object import OMBaseObject

class GeoLayer(OMBaseObject):
    tid = "geolayer"
    _TID_FRIENDLY_NAME = 'Geologic Layers'
 
    _ATTRIBUTES = OrderedDict()

    _ATTRIBUTES['value'] = {
        'default_value': 0.0,
        'type': float      
    }      
    
    _ATTRIBUTES['vp'] = {
        'default_value': 0.0,
        'type': float      
    }  
    _ATTRIBUTES['rho'] = {
        'default_value': 0.0,
        'type': float      
    }        

    
    _SHOWN_ATTRIBUTES = [
                            ('value', 'Value'),
                            ('vp', 'Vp'),
                            ('rho', 'Rho')
    ]   

 
    
    def __init__(self, **attributes):
        super().__init__(**attributes)