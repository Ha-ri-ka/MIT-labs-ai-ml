#additional ques1 Generate a 1-D array of 10 random integers. 
#Each integer should be a number between 30 and 40 (inclusive).
import numpy as np
import random as rn
randArray=np.empty((1,10),dtype=int)
for i in range(10):
    randArray[0][i]=rn.randint(30,40)
randArray

#output
#array([[40, 31, 35, 31, 37, 40, 35, 31, 32, 33]])
