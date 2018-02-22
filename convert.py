import matplotlib.pyplot as plt

nArr = [2**(i+1) for i in range(8)]
avg = [60.576, 73.140, 83.360, 90.478, 94.668, 97.001, 98.210, 98.798]

plt.plot(nArr,avg,'bo',nArr,avg,'k')
plt.xlabel("n")
plt.ylabel("Average")
plt.title("Per-agent average value (1000 trials)")
plt.show()
