from multiprocessing import Pool, TimeoutError
import time
import os
import asyncio

def eyes(x):
    return x*x*x*x*x*x

def mouth(x):
    return x*x*x*x*x*x

def headH(x):
    return x*x*x*x*x*x

def headV(x):
    return x*x*x*x*x*x

def getFeatures():
    start = time.time()

    res0 = eyes(10)      
    print(res0)     

    res1 = mouth(10)     
    print(res1)      

    res2 = headH(10)     
    print(res2)      

    res3 = headV(10)    
    print(res3)              

    print("For the moment, the pool remains available for more work")

    et = time.time() - start
    print(et)
if __name__ == '__main__':
    getFeatures()
    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")