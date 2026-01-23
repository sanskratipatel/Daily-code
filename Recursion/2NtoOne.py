def ntoOne(n):
    if n==0:
        return n 
    print(n)
    ntoOne(n-1)  

ans = ntoOne(10)