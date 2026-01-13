class ValueTooHigh(Exception) :
    pass 

def high (x) :
    if x >100 :
        raise ValueTooHigh("vALUE TOO HIGH") 

try:
    high(1000) 
except Exception as e :
    print(str(e))