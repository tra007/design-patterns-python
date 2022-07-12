from abc import ABC,abstractmethod

class TvState(ABC):
    
    @abstractmethod
    def doAction(self):
        pass

class TvOn(TvState):

    def doAction(self):
        print("tv on")

class TvOff(TvState):

    def doAction(self):
        print("tv off")

class TVContext:
    def __init__(self,action:TvState) -> None:
        self.__action=action
    
    @property
    def action(self):
        return self.__action
    
    @action.setter
    def action(self,action):
        self.__action=action
    
    def doAction(self):
        self.__action.doAction()

t1=TVContext(TvOn())
t2=TVContext(TvOff())
t1.doAction()
t2.doAction()