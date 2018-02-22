from auction import randomAuction, runAuction
from generateTxt import generateText
import matplotlib.pyplot as plt
import time
import subprocess

n = 256

mArr = [10**(i+1) for i in range(2)]
print "Will run auction algorithm for values of m = ", mArr

avgAuction = []
avgLP = []
avgGen = []

for m in mArr:
    print "Starting at m = ", m
    totalTimeAuction = 0
    totalTimeLP = 0
    generateTime = 0
    for i in range(1):
        if i % 10 == 0:
            print "At iteration: ", i

        startTime = time.time()
        V = randomAuction(n,m)[2]
        totalTimeAuction += time.time()-startTime
        startTime = time.time()
        generateText(V)
        #print V
        generateTime += time.time()-startTime
        startTime = time.time()
        subprocess.call(["glpsol","--model","output.txt"])
        totalTimeLP += time.time()-startTime

    print "Done with m = ", m
    avgAuction.append(totalTimeAuction/100.0)
    avgLP.append(totalTimeLP/100)
    avgGen.append(generateTime/100)
print "Auction times", avgAuction
print "GLPK times", avgLP
print "Generate GLPK file times", avgGen
#f, axarr = plt.subplots(3, sharex=True)
#f.suptitle("Time (s) for Auction Algorithm and GLPK (100 trials at n=128)")
plt.plot(mArr,avgAuction,'bo')
plt.plot(mArr,avgAuction,'b')
plt.title("Time (s) for Auction Algorithm (100 trials at n=256)")
plt.xlabel("M")
plt.ylabel("Time(s)")
plt.savefig("516/auction.png")

plt.plot(mArr,avgLP,'ro')
plt.plot(mArr,avgLP,'r')
plt.title("Time (s) for GLPK (100 trials at n=256)")
plt.xlabel("M")
plt.ylabel("Time(s)")
plt.savefig("516/glpk.png")

plt.plot(mArr,avgAuction,'bo',mArr,avgLP,'ro')
plt.plot(mArr,avgAuction,'b',mArr,avgLP,'r')
plt.title("Time (s) for Auction Algorithm and GLPK (100 trials at n=256)")
plt.xlabel("M")
plt.ylabel("Time(s)")
plt.savefig("516/auctionGlpk.png")
plt.show()
#60576, 73140, 83360, 90478, 94668, 97001, 98210, 98798
