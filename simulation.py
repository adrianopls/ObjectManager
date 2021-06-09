
from collections import OrderedDict

from .density import Density


class Simulation(Density):
    tid = 'simulation'
    _TID_FRIENDLY_NAME = 'Simulation'


    _ATTRIBUTES = OrderedDict()

    # _ATTRIBUTES['_type'] = {
    #     'default_value': "Ricker",
    #     'type': str      
    # }    
    
    # _ATTRIBUTES['points_x'] = {
    #     'default_value': 0.0,
    #     'type': int      
    # }       
    
    _ATTRIBUTES['dx'] = {
        'default_value': 0.0,
        'type': float      
    }   
    
    # _ATTRIBUTES['points_y'] = {
    #     'default_value': 0.0,
    #     'type': float      
    # }       
    
    _ATTRIBUTES['dy'] = {
        'default_value': 0.0,
        'type': float      
    }      

    _ATTRIBUTES['dt'] = {
        'default_value': 0.0,
        'type': float      
    }      
    
    _ATTRIBUTES['sou_x'] = {
        'default_value': 0,
        'type': int      
    }      

    _ATTRIBUTES['sou_y'] = {
        'default_value': 0,
        'type': int      
    }   

    _ATTRIBUTES['model_uid'] = {
        'default_value': 0,
        'type': str
    }      

    _ATTRIBUTES['wavelet_uid'] = {
        'default_value': "",
        'type': str      
    }   

    _ATTRIBUTES['cfl'] = {
        'default_value': 0.0,
        'type': float      
    }   
    
    _ATTRIBUTES['c1'] = {
        'default_value': 0.0,
        'type': float      
    }   
    
    _SHOWN_ATTRIBUTES = [('nx', 'Points X'),
                          ('dx', 'Dx'),
                          ('ny', 'Points Y'),
                          ('dy', 'Dy'),
                          ('nt', 'Sim Steps'),
                          ('dt', 'Time Step'),
                          ('sou_x', 'Source X'),
                          ('sou_y', 'Source Y'),
                          ('max', 'Max'),
                          ('min', 'Min'),
                          ('cfl', 'CFL'),
                          ('c1', 'Gridpoints per Wavelenght'),
    ]

    def __init__(self, data, **attributes):
        super().__init__(data, **attributes)

    
    @property
    def nx(self):
        if self._data is None:
            return None
        return self._data.shape[-1]

    @property
    def ny(self):
        if self._data is None:
            return None
        return self._data.shape[-2]
       
    @property
    def nt(self):
        if self._data is None:
            return None
        return self._data.shape[0]   