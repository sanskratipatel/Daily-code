# Strategy Design Pattern 
from abc import ABC, abstractmethod

class Talkable(ABC) :
    @abstractmethod
    def talk(self):
         pass 
class NormalTalk(Talkable): 
    def __init__(self):
         pass 
    
    def talk(self):
         return (f"Normal Talking **************** ") 

class NoTalk(Talkable) :
    def __init__(self):
          pass 
    
    def talk(self):
        return ("No talk *************") 
    
class Walkable(ABC) :
    @abstractmethod 
    def walk(self):
         pass 

class NormalWalk(Walkable): 
    def __init__(self):
         pass 
    
    def walk(self):
         return (f"Normal walking **************** ") 

class NoWalk(Walkable) :
    def __init__(self):
          pass 
    
    def walk(self):
        return ("No Walk *************") 
    


class Flyable(ABC):
    @abstractmethod
    def fly(self):
         pass
    

class NormalFly(Flyable): 
    def __init__(self):
         pass 
    
    def fly(self):
         return (f"Normal Flying **************** ") 

class NoFly(Flyable) :
    def __init__(self):
          pass 
    
    def fly(self):
        return ("No Flying *************")  

class JetFly(Flyable) :
    def __init__(self):
          pass 
    
    def fly(self):
        return ("JetFlying *************")  

class Robot (ABC): 
    def __init__(self , walkable: Walkable , talkable : Talkable , flyable:Flyable):
         self.talkable = talkable 
         self.walkable = walkable 
         self.flyable = flyable 
    
    def walk(self) : 
        return self.walkable.walk() 
    
    def talk(self):
       return self.talkable.talk() 
    def fly(self):
       return self.flyable.fly()

    @abstractmethod
    def projection(self):
         pass 


class CompainonRobot(Robot) : 
    def __init__(self, walkable, talkable, flyable):
         super().__init__(walkable, talkable, flyable) 
    
    def projection(self):
        return ("Robot Project class") 


class WorkerRobot(Robot):
    def __init__(self, walkable, talkable, flyable):
        super().__init__(walkable, talkable, flyable)

    def projection(self):
        return ("Worker Robot Projection")


robot1 = CompainonRobot(  NormalWalk(),
    NormalTalk(),
    NoFly()) 
print(robot1.walk())
print(robot1.talk())
print(robot1.fly())
robot2 = WorkerRobot( 
      NormalWalk(),NoTalk() , NormalFly()
) 
print(robot2.walk())
print(robot2.talk())
print(robot2.fly())
robot3 = WorkerRobot( 
      NoWalk(),NormalTalk() , NormalFly()
) 
print(robot3.walk())
print(robot3.talk())
print(robot3.fly())