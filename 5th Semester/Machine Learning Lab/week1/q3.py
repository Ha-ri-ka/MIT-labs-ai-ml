#question 3 Find the positions of:
#elements in x where its value is more than its corresponding element in y,
#and elements in x where its value is equals to its corresponding element in y.
import numpy as np
x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89]) 
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])
same_as_y=[]
more_than_y=[]
if len(x)<len(y): size=len(x)
else: size=len(y)
i=j=0
for ind in range (size):
    if(x[ind]==y[ind]):
        same_as_y.append(ind)        
    elif(x[ind]>y[ind]):
        more_than_y.append(ind)    
np.array(more_than_y)
np.array(same_as_y)

#question 3 without for loop
import numpy as np
x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89]) 
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])
np.where(x>y)
np.where(x==y)

#output
#array([1, 2, 4, 5, 6, 7, 8, 9])
#array([0])
