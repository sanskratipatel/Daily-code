def oneTon(n):
    if (n == 0) :
        return 1 
    oneTon(n-1) 
    print(n) 


ans = oneTon(9) 
