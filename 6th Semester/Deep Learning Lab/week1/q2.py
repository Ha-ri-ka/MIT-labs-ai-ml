import torch
#permute allows us to re-shape the tensor using the indices corresponding to original tensor's dimensions.
#so, if our original tensor has a dimension of (2,3,4) and we want to reshape it to be (3,4,2) then we can use the indices (0,1,2) and change them to
#(1,2,0) using permute. This creates a new tensor of the dimensions (3,4,2).
#syntax: og_tensor.permute(ind1,ind2,ind3)
tens=torch.ones(size=(2,3,4))
print('orignal tensor:\n',tens)
permuted_tens=tens.permute(1,2,0)
print('permuted tensor:\n',permuted_tens)