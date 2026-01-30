def reverseWords(s):
        # code here
        parts = s.split(".")  
        print(parts)
        rev = []
        for i in range(len(parts)-1 , -1, -1) : 
            if parts[i] != "":
               rev.append(parts[i]) 
            
        return ".".join(rev) 

print(reverseWords(".i.like.this.program.very.much.") )
