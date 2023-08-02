#question 4 Extract the first four columns of this 2-D array
import numpy as np
Assign_4= np.arange(100).reshape(5,-1)
Assign_4[:,0:4]

#output
#array([[ 0,  1,  2,  3],
#      [20, 21, 22, 23],
#      [40, 41, 42, 43],
#      [60, 61, 62, 63],
#      [80, 81, 82, 83]])
