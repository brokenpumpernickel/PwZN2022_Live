import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def fibon(n):
    if n < 2:
        return n
    
    return fibon(n - 1) + fibon(n - 2)

def fibon_job(n):
    val = fibon(n)

    return n, val

def hello_world():
    print('Hello World from Function')
    return 'Hello World'

if __name__ == '__main__':
    # start = time.time()
    # for n in range(40):
    #     print(f'{n} -> {fibon(n)}')
    # stop = time.time()
    # print(f'{stop - start = }')

    # with ProcessPoolExecutor(24) as ex:
    #     futures = [ex.submit(hello_world) for _ in range(10)]
    #     for f in futures:
    #         print(f.result())

    start = time.time()
    with ProcessPoolExecutor(24) as ex:
        futures = [ex.submit(fibon_job, n) for n in range(60)]
        for f in as_completed(futures):
            print(f.result())
    stop = time.time()            
    print(f'{stop - start = }')            
    