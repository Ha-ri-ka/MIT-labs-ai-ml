#question 2  Replace all odd numbers in the given array with -1
import numpy as np
og_array=np.array([0,1,2,3,4,5,6,7,8,9])
new_array=np.zeros(len(og_array),dtype=int)
i=0
for ele in og_array:
    if ele%2!=0:
        new_array[i]=-1
    else:
        new_array[i]=ele
    i+=1    
new_array

#question 2 without for loop
import numpy as np
og_array=np.array([0,1,2,3,4,5,6,7,8,9])

og_array[og_array%2!=0]=-1
og_array

#output
#array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])

