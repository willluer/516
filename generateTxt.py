import numpy as np
import math

def generateText(V):
    V = np.array(V).flatten()
    n = len(V)
    dummy = np.array(range(n)).reshape(math.sqrt(n),-1)
    #print dummy
    txt = ""

    #GENERATE VARIABLES
    for i in range(n):
        txt += "var x" + str(i) + " >= 0;\n"
    txt += "\n"


    #GENERATE EQUATION TO BE MAXIMIZED
    txt += "maximize sum: "

    i = 0
    for v in V:
        if i == len(V)-1:
            txt += "" + str(v) + "*x" + str(i) + ";"
        else:
            txt += "" + str(v) + "*x" + str(i) + " + "
        i += 1
    txt += "\n\n"

    #GENERATE CONSTRAINTS

    #Row constraints
    for row in range(len(dummy)):
        txt += "s.t. row"+str(row)+": "
        for col in range(len(dummy)):
            if col == len(dummy)-1:
                txt += "x" + str(dummy[row][col])
            else:
                txt += "x" + str(dummy[row][col]) + " + "
        txt += " = 1; \n"


    #Column constraints
    for row in range(len(dummy)):
        txt += "s.t. col"+str(row)+": "
        for col in range(len(dummy)):
            if col == len(dummy)-1:
                txt += "x" + str(dummy[col][row])
            else:
                txt += "x" + str(dummy[col][row]) + " + "
        txt += " = 1; \n"
    #print txt

    txt += "end;"
    text_file = open("output.txt", "w")
    text_file.write(txt)
    text_file.close()


# V = [
# [89, 42, 0, 2, 24, 20, 40, 37, 30, 77],
# [66, 75, 9, 59, 69, 66, 52, 14, 85, 36],
# [82, 68, 0, 81, 36, 25, 48, 53, 11, 68],
# [6, 96, 82, 53, 17, 70, 26, 12, 91, 82],
# [34, 86, 22, 18, 66, 73, 82, 88, 18, 36],
# [90, 43, 43, 93, 80, 96, 12, 28, 74, 93],
# [19, 75, 30, 48, 31, 76, 84, 29, 20, 15],
# [29, 73, 88, 9, 36, 40, 40, 19, 1, 45],
# [77, 31, 6, 68, 36, 40, 22, 43, 27, 61],
# [70, 21, 2, 89, 30, 91, 66, 74, 79, 92]]
#

#generateText(V)
