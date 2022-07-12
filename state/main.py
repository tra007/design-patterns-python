# ------------- whit out state -----------------
# from enum import Enum, auto
# class ToolType(Enum):
#     SELECTION=auto()
#     BRUSH=auto()
#     ERASER=auto

# class Canvas:
#     def __init__(self,currentTool) -> None:
#         self.__currentTool=currentTool
    
#     @property
#     def currentTool(self):
#         return self.__currentTool
    
#     @property.setter
#     def currentTool(self,currentTool):
#         self.__currentTool=currentTool
    
#     def mouseDown(self):
#         if self.__currentTool==ToolType.SELECTION:
#             print("selection icon")
#         elif self.__currentTool==ToolType.BRUSH:
#             print("brush icon")
#         elif self.__currentTool==ToolType.ERASER:
#             print("eraser icon")
#     def mouseUp(self):
#         if self.__currentTool==ToolType.SELECTION:
#             print("draw dashed rectangle")
#         elif self.__currentTool==ToolType.BRUSH:
#             print("draw line")
#         elif self.__currentTool==ToolType.ERASER:
#             print("Erase something")

#------------- state pattern -------------------------

from abc import ABC,abstractmethod

class Tool(ABC):

    @abstractmethod
    def mouseDown(self):
        pass
    @abstractmethod
    def mouseUp(self):
        pass

class SelectionTool(Tool):
    
    def mouseUp(self):
        print("Selection Icon")

    def mouseDown(self):
        print("draw a dashed rectangle")

class BrushTool(Tool):
    
    def mouseUp(self):
        print("Brush Icon")

    def mouseDown(self):
        print("draw a Line")
 
class EraserTool(Tool):
    
    def mouseUp(self):
        print("Eraser Icon")

    def mouseDown(self):
        print("Erase page")

class Canvas:

    def __init__(self,currentTool:Tool) -> None:
        self.__currentTool=currentTool
    
    @property
    def currentTool(self):
        return self.__currentTool
    
    @currentTool.setter
    def currentTool(self,currentTool:Tool):
        self.__currentTool=currentTool
    
    def mouseUp(self):
        self.__currentTool.mouseUp()
    
    def mouseDown(self):
        self.__currentTool.mouseDown()

t1=Canvas(EraserTool())
print(t1.currentTool)
t1.mouseUp()
t1.mouseDown()
