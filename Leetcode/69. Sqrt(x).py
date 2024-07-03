    def mySqrt(x):
        if x<2:
            return x
        
        
        z = (x+1)/2
        while abs(x-z)>=0.00001:
            y = z
            z = (y+x/y)/2
        return round(z)