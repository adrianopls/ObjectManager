
from collections import OrderedDict

from .manager import ObjectManager
from .object import OMBaseObject
#from .density import Density


class Model2DAcoustic(OMBaseObject): #(Density):
    tid = 'acoustic_2d_model'
    _TID_FRIENDLY_NAME = '2D Acoustic Model'


    _ATTRIBUTES = OrderedDict()     
    _ATTRIBUTES['image_uid'] = {
        'default_value': 0,
        'type': str
    }   
    
    
    _ATTRIBUTES['nx'] = {
        'default_value': 0,
        'type': int 
    }   
         
    
    _ATTRIBUTES['ny'] = {
        'default_value': 0,
        'type': int    
    }   
    
    _ATTRIBUTES['dx'] = {
        'default_value': 0.0,
        'type': float      
    }   
         
    
    _ATTRIBUTES['dy'] = {
        'default_value': 0.0,
        'type': float      
    }      

    
    _SHOWN_ATTRIBUTES = [
                          ("image", "Image"),  
                          ('nx', 'Points X'),
                          ('dx', 'Dx'),
                          ('ny', 'Points Y'),
                          ('dy', 'Dy')
    ]


    def __init__(self, **attributes):
        super().__init__(**attributes)


    def _get_image(self):
        OM = ObjectManager()
        return OM.get(self.image_uid) 
    
    
        
    @property
    def image(self):
        image = self._get_image()
        return image.name
        
    
    @property
    def nx(self):
        image = self._get_image()
        # image.width
        print("\nnx: " + str(image._data.shape[1]))
        return image._data.shape[1]
        
    @property
    def ny(self):
        image = self._get_image()
        print("\nny: " + str(image._data.shape[0]))
        return image._data.shape[0]
    
    
    def get_porosity(self, pore_layer_value):
        OM = ObjectManager()
        image = self._get_image()
        
        layers = OM.list(parent_uid=self.uid)
        if len(layers) != 2:
            raise Exception("")

        total_pixels = self.nx * self.ny        
        pore_count = (image.data == pore_layer_value).sum()
        
        return pore_count/total_pixels
            
        
    
    