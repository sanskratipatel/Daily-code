class DocumentEditor:  
    document_element = [] 
    render_element = None
    def __init__(self):
          pass  
    
    def add_text(self,text):
         self.document_element.append(text) 
    
    def add_images(self,image_path): 
        self.document_element.append(image_path) 
    
    def render_document(self) : 
        if (self.render_element is None) :  
            result = ""
            for ele in self.document_element:
                if (len(ele))>4 and  (ele[-4:] ==".jpg" or ele[-4:] ==".png") :  
                    result = result + "[Images : "+ ele + "]" + "\n"
                else: 
                    result = result + ele + "\n"
            self.render_element = result
        return self.render_element
    
    def save_to_file(self , filename = "document.txt") : 
        content = self.render_document() 
        try: 
            with open(filename , "w") as file: 
                file.write(content)
        except Exception as e :
            print("Error While save file ",str(e))



# This file break Solid Princeple 1 and 2 
d1 = DocumentEditor() 
d1.add_text("Hello") 
d1.add_images("23223ee.png") 
print(d1.render_document()) 
d1.save_to_file()