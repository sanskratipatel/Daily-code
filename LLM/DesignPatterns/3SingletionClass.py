# This is Have only one object this is called singleton class 

class SingletonClass: 
    __instance = None 
    __initialized = False 

    def __new__( cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls) 
        return cls.__instance
    def __init__(self): 
        if not self.__initialized :
            print("Singleton Constructor Called") 
            self.__initialized = True

s1 = SingletonClass() 
s2 = SingletonClass() 
print(s1 ==s2 ) 
