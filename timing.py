from auction import randomAuction, runAuction
from generateTxt import generateText
import matplotlib.pyplot as plt
import time
import subprocess

n = 50

mArr = [10**(i+1) for i in range(6)]
print "Will run auction algorithm for values of m = ", mArr

avgAuction = []
avgLP = []

for m in mArr:
    print "Starting at m = ", m
    totalTimeAuction = 0
    totalTimeLP = 0
    for i in range(100):
        if i % 10 == 0:
            print "At iteration: ", i

        startTime = time.time()
        V = randomAuction(n,m)[2]
        totalTimeAuction += time.time()-startTime
        generateText(V)
        startTime = time.time()
        subprocess.call(["glpsol","--model","output.txt","--output","results.txt"])
        totalTimeLP += time.time()-startTime

    print "Done with m = ", m
    avgAuction.append(totalTimeAuction/100.0)
    avgLP.append(totalTimeLP/100)

print avgAuction
print avgLP
f, axarr = plt.subplots(2, sharex=True)
f.suptitle("Time (s) for Auction Algorithm and GLPK (100 trials at n=50)")
axarr[0].plot(mArr,avgAuction,'bo')
axarr[0].plot(mArr,avgAuction,'b')
axarr[0].set_xlabel("Auction")

axarr[1].plot(mArr,avgLP,'ro')
axarr[1].plot(mArr,avgLP,'r')
axarr[1].set_xlabel("GLPK")


plt.show()
#60576, 73140, 83360, 90478, 94668, 97001, 98210, 98798
