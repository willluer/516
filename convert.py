import matplotlib.pyplot as plt
import math

avgAuction = [0.15325873851776123, 0.15123460531234742, 0.15328933000564576, 0.15158798456192016,0.14912256717681885, 0.14858983755111693]
avgLP = [1.9812445259094238, 1.9489335227012634, 1.9596352005004882, 1.9329039859771728,1.926978225708008, 1.9200935125350953]
avgGen = [0.582164101600647, 0.5841753721237183, 0.5822093439102173, 0.5822297620773316,0.5736639499664307, 0.5685700941085815]

mArr = [math.log(10**(i+1)) for i in range(6)]

#for i in range(len(mArr)):
    #mArr[i] = math.log(mArr[i])

#print mArr

# plt.plot(mArr,avgAuction,'bo')
# plt.plot(mArr,avgAuction,'b')
# plt.title("Time (s) for Auction Algorithm (100 trials at n=256)")
# plt.xlabel("log(M)")
# plt.ylabel("Time (s)")
# #plt.ylim(ymin=0)
# # plt.show()
# plt.savefig("516/auction.png")
#
# plt.clf()
# plt.plot(mArr,avgLP,'ro')
# plt.plot(mArr,avgLP,'r')
# plt.title("Time (s) for GLPK (100 trials at n=256)")
# plt.xlabel("log(M)")
# plt.ylabel("Time (s)")
# plt.savefig("516/glpk.png")
# plt.show()

plt.clf()
plt.plot(mArr,avgAuction,'bo',mArr,avgLP,'ro')
plt.plot(mArr,avgLP,'r',label="GLPK")
plt.plot(mArr,avgAuction,'b', label="Auction")
plt.title("Time (s) for Auction Algorithm and GLPK (100 trials at n=256)")
plt.xlabel("log(M)")
plt.ylabel("Time (s)")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.savefig("516/auctionGlpk.png")
plt.show()
