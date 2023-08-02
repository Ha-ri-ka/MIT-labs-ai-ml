#additional ques2
import numpy as np
A= np.array(((1, 2, 3), (4, 5, 6), (7, 8, 10)))
B = np.array(((7, 8, 10) ,(4, 5, 6), (1, 2, 3)))
#i) Add and Subtract of the Matrix A and B, print the resultant matrix C for add and E for subtract.
C=A+B
E=A-B
#ii)Compute the sum of all elements of Matrix A, sum of each column of Matrix B and sum of each row of Matrix C
A.sum()

col_sum=[]
for i in range (len(B[0])):
    col_sum.append(B[:,i].sum())
col_sum


#iii) Product of two matrices A and B, and print the resultant matrix D
D=A@B
