from abc import ABC, abstractmethod

class DocumentElement(ABC): 
    @abstractmethod
    def render(self): 
        pass 

class TextElement(DocumentElement) :
    # text = "" 
    def __init__(self, text):
        self.text = text 
    
    def render(self):
        return self.text  
    
class ImangeElement(DocumentElement) :
    # imagepath = "" 
    def __init__(self , imagepath):  
        self.imagepath = imagepath 
    
    def render(self):
        return "[Image: " + self.imagepath + "]"


class NewLineElement(DocumentElement) :
    def __init__(self): 
        pass 

    def render(self):
        return "\n" 
    

class TabSpaceElement(DocumentElement):
    def __init__(self):
        pass 

    def render(self):
        return "\t"
    

class Document:
    document_element = [] 
    def add_element(self , element):
        self.document_element.append(element) 
    

    def render(self): 
        result = "" 
        for element in self.document_element : 
            result = result + element.render() 
        
        return result


class Persistence(ABC):
    
    @abstractmethod
    def save(self ,data):
        pass


class FileStorage(Persistence):
    def __init__(self,filename = "documents.txt"):
       self.filename =filename 

    def save(self,data ):
        content =data 
        try: 
            with open(self.filename  ,"w") as file:  
                file.write(content)
        except Exception as e : 
            print("Error During save in file " ,str(e))


class DatabaseSave(Persistence) :
    def __init__(self):
        pass 

    def save(self, data):
        print("Saving into Database ", data) 

class DocumentEditor :
    def __init__(self,document : Document,persistence :Persistence):
        self.document=document 
        self.persistence = persistence
    
    def add_text(self,text) :
        self.document.add_element(TextElement(text))
     
    def add_image(self,image):
        self.document.add_element(ImangeElement(image)) 

    def add_new_line(self):
        self.document.add_element(NewLineElement()) 

    def add_tab(self) :
        self.document.add_element(TabSpaceElement()) 

    def render(self) :
        return self.document.render() 

    def save(self) :
        content = self.render() 
        self.persistence.save(content) 


doc = Document()
storage = FileStorage("mydoc.txt")

editor = DocumentEditor(doc, storage)

editor.add_text("Hello")
editor.add_new_line()
editor.add_tab()
editor.add_text("World")
editor.add_new_line()
editor.add_image("photo.png")

editor.save()
