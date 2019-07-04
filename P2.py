def anonymous(x):
    return x**2 + 1

def intergrate(fun,start,end):
    step = 0.0001
    intercept = start
    area = 0
    
    while intercept < end:
        intercept += step
        
        # upper height 
        area += step*fun(intercept)
        
        # lower height
        #area += step*fun(intercept - step)
    
    return area



print(intergrate(anonymous,0,10))
        
        