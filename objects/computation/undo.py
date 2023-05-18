class undoobj:
    def __init__(self, pos:tuple,fromundo:int,toundo:int):
        self.pos=pos
        self.fromundo=fromundo
        self.toundo=toundo

class undo:
    def __init__(self) -> None:
        self.undo_stack=[]
        self.redo_stack=[]
        self.isOpen=False
        self.openedBy=None

    def open_container(self,openedBy:str):
        if(not self.isOpen):
            self.new_stack=[]
            self.isOpen=True
            self.openedBy=openedBy

    def add(self, pos:tuple,fromundo:int,toundo:int):
       if(self.isOpen):
           uo=undoobj(pos,fromundo,toundo)
           if(len(self.new_stack)>0):
               if(not self.compare(self.new_stack[-1],uo)):
                   self.new_stack.append(uo)
           else:
                self.new_stack.append(uo)
           
    def compare(self,undo1,undo2):
        if(undo1.pos==undo2.pos and undo1.fromundo==undo2.fromundo and undo1.toundo==undo2.toundo):
            return True
        else:
            return False

    def close_container(self,openedBy:str):
        if(self.isOpen and self.openedBy==openedBy):
            self.undo_stack.append(self.new_stack)
            # print(self.new_stack)
            self.new_stack=[]

