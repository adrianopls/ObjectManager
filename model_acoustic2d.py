
from collections import OrderedDict

from .density import Density


class Model2DAcoustic(Density):
    tid = 'acoustic_2d_model'
    _TID_FRIENDLY_NAME = '2D Acoustic Model'


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

    
    _SHOWN_ATTRIBUTES = [('nx', 'Points X'),
                          ('dx', 'Dx'),
                          ('ny', 'Points Y'),
                          ('dy', 'Dy')
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
    
    
    