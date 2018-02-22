from auction import randomAuction, runAuction
from generateTxt import generateText
import matplotlib.pyplot as plt

n = 10
M = 100

nArr = [2**(i+1) for i in range(4)]
print "Will run auction algorithm for values of n = ", nArr
avg = []

for n in nArr:
    print "Starting at n = ", n
    total = 0
    for i in range(1000):
        if i % 200 == 0:
            print "At iteration: ", i
        total += randomAuction(n,M)[1]
    print "Done with n = ", n
    avg.append(total/(n*1000))
    print avg

#print avg
plt.plot(nArr,avg,'bo',nArr,avg,'k')
plt.xlabel("n")
plt.ylabel("Average")
plt.title("Per-agent average value (1000 trials)")
plt.show()
print avg
#60576, 73140, 83360, 90478, 94668, 97001, 98210, 98798
