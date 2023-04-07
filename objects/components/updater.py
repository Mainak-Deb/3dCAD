import sys
sys.path.append('./')

class updater:
    __instances=[]
    def __init__(self):
        updater.__instances.append(self)
        
    @classmethod
    def update(cls,event):
        obj_array=cls.__instances
        for i in obj_array:
            i.update(event)
    
    @classmethod
    def draw(cls):
        obj_array=cls.__instances
        for i in obj_array:
            i.draw()
    
