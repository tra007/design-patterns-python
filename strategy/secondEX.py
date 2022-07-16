from abc import ABC,abstractmethod

class IStrategy(ABC):
    
    @abstractmethod
    def getTravelTime(self):
        pass

class CarStrategy(IStrategy):

    def getTravelTime(self):
        print("15")

class BikeStrategy(IStrategy):

    def getTravelTime(self):
        print("25")

class BusStrategy(IStrategy):

    def getTravelTime(self):
        print("13")


class TravelStrategy:
    __strategy=None

    def __init__(self,strategy) -> None:
        self.__strategy=strategy
    
    def getTravelTime(self):
        self.__strategy.getTravelTime()

# a1=TravelStrategy(BikeStrategy())
a1=TravelStrategy(CarStrategy())
a1.getTravelTime()