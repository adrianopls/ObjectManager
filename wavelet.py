
from collections import OrderedDict

import numpy as np

from .object import OMBaseObject


class Wavelet(OMBaseObject):
    tid = "wavelet"
    _TID_FRIENDLY_NAME = "Wavelet"
 
    _ATTRIBUTES = OrderedDict()

    _ATTRIBUTES['_type'] = {
        'default_value': "Ricker",
        'type': str      
    }      
    _ATTRIBUTES['f0'] = {
        'default_value': 0.0,
        'type': float      
    }        
    _ATTRIBUTES['amp'] = {
        'default_value': 0.0,
        'type': float      
    }      

    _SHOWN_ATTRIBUTES = [
                            ('_type', 'Type'),
                            ('f0', 'Base freq'),
                            ('amp', 'Amplitude')
    ]   

    
    def __init__(self, **attributes):
        super().__init__(**attributes)
        
        
    def get_amplitude_data(self, time_data):
        # ## Source signal - Ricker-wavelet
        tau = np.pi * self.f0 * (time_data - 1.5 / self.f0)
        print('tau')
        print(tau.min(), tau.max())    
        return self.amp * (1.0 - 2.0 * tau**2.0) * np.exp(-tau**2)