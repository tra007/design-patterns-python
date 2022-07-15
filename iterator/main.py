# class BrowseHistory:
#     __urls=[]

#     @property
#     def urls(self):
#         return self.__urls
#     def push(self,url):
#         self.__urls.append(url)
    
#     def pop(self):
#         self.__urls.pop()

# t1= BrowseHistory()
# t1.push("A")
# t1.push("B")
# t1.push("C")
# print(t1.urls)
# for i in t1.urls:
#     print(i)

from abc import ABC,abstractmethod
class Iterator(ABC):
    
    @abstractmethod
    def hasNext() -> bool:
        pass

    @abstractmethod
    def current() -> str:
        pass
    
    @abstractmethod
    def next() -> None:
        pass

class BrowseHistory:
    __urls=[]

    @property
    def urls(self):
        return self.__urls

    def createIterator(self):
        return self.ListIterator(self)
    
    def push(self,url):
        self.urls.append(url)
    
    def pop(self):
        self.urls.pop()

    class ListIterator(Iterator):
        __history=None
        __index=0
      
        def __init__(self,history) -> None:
            self.__history=history
        
        def hasNext(self)->bool:
            return self.__index<len(self.__history.urls)
      
        def current(self):
            return self.__history.urls[self.__index]
      
        def next(self):
            self.__index+=1
    
    
t1= BrowseHistory()
t1.push("A")
t1.push("B")
t1.push("C")
m1 = t1.createIterator()
while (m1.hasNext()):
    url=m1.current()
    print(url)
    m1.next()