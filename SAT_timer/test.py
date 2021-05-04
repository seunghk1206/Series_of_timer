import time
import sys
def timer(NoS):
    start1 = time.time()
    totalTime = 0
    for remaining in range(NoS, 0, -1):
        start = time.time()
        a = remaining-(3600*(remaining//3600))
        b = a//60
        c = remaining-(remaining//3600*3600)-(b*60)
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        print(remaining//3600, ':', b, ':', c)
        time.sleep(1-(time.time()-start)-0.0083)
        totalTime += time.time()-start
        print(time.time()-start)
    print("average: " + str(totalTime/NoS))
    print(time.time()-start1)
    time.sleep(5)

timer(7200)
'''
import time
import sys
def timer(NoS):
    start1 = time.time()
    totalTime = 0
    for remaining in range(NoS, 0, -1):
        start = time.time()
        a = remaining-(3600*(remaining//3600))
        b = a//60
        c = remaining-(remaining//3600*3600)-(b*60)
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        print(remaining//3600, ':', b, ':', c)
        time.sleep(1-(time.time()-start)-0.0083)
        totalTime += time.time()-start
        print(time.time()-start)
    print("average: " + str(totalTime/NoS))
    print(time.time()-start1)
    time.sleep(5)

timer(60)
'''