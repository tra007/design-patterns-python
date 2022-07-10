# Memento
class EditorState:

    def __init__(self,content) -> None:
        self.__content=content
    
    @property
    def content(self):
        return self.__content

# Originator
class Editor:
    __content= "" 

    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self,content):
        self.__content=content
    
    def createState(self):
        return EditorState(self.content)
    
    def restore(self,state:EditorState):
        self.__content=state.content

# Create Taker
class History:
    states=[]

    def save(self,state:EditorState):
        self.states.append(state)

    def revert(self,editor:Editor):
        if len(self.states)>0:
            editor.restore(self.states.pop())
        else:
            print("empty")

editor =Editor()
history = History()
editor.content="this"
history.save(editor.createState())
editor.content="this is"
history.save(editor.createState())
editor.content="this is test"
print(editor.content) # this is test
history.revert(editor) 
print(editor.content) # this is
history.revert(editor)
print(editor.content) #this
history.revert(editor)# empty

