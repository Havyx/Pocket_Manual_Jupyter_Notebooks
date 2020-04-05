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

@asyncio.coroutine
async def getFeatures():
    start = time.time()
    with Pool(processes=4) as pool:
    
        res0 = pool.apply_async(eyes, (10,))      
        print(res0.get(timeout=1))     
        res1 = pool.apply_async(mouth, (10,))      
        print(res1.get(timeout=1))      
        res2 = pool.apply_async(headH, (10,))      
        print(res2.get(timeout=1))      
        res3 = pool.apply_async(headV, (10,))      
        print(res3.get(timeout=1))              
        print("For the moment, the pool remains available for more work")
    
    et = time.time() - start
    print(et)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getFeatures())
    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")