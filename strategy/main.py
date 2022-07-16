from abc import ABC,abstractmethod

class Compressor(ABC):
    
    @abstractmethod
    def compress(self,fileName):
        pass

class Filter(ABC):
    
    @abstractmethod
    def apply(self,fileName):
        pass

class JpegCompressor(Compressor):

    def compress(self, fileName):
        print("Compressing using Jpeg")

class PngCompressor(Compressor):

    def compress(self, fileName):
        print("Compressing using PNG")

class BlackAnDWitheFilter(Filter):

    def apply(self, fileName):
        print("Apply black and white")


class ImageStorage:
    __compressor=None
    __filter=None
    
    def __init__(self,compressor,filter):
        self.__compressor=compressor
        self.__filter=filter

    def store(self,fileName):
        self.__compressor.compress(fileName)
        self.__filter.apply(fileName)

img=ImageStorage(JpegCompressor(),BlackAnDWitheFilter())
img.store("al")
# img.store("al",JpegCompressor(),BlackAnDWitheFilter())
