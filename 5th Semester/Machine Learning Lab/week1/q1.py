#question 1  Convert a 1-D array into a 2-D array with 3 rows.
import numpy as np
og_array=np.array([0,1,2,3,4,5,6,7,8])
new_array=og_array.reshape(3,3)
new_array

#OUTPUT
#array([[0, 1, 2],
#      [3, 4, 5],
#     [6, 7, 8]])
