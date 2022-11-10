def get_summation(n):
    
    if n == 1:
        return n
    else:
        return n+get_summation(n-1)