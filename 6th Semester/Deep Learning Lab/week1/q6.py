import torch

tensor=torch.rand(size=(7,7))
print('tensor from Q5:\n',tensor)
randomTensor=torch.rand(size=(1,7))
print('random tensor:\n',randomTensor)
transposedRandTens=randomTensor.permute(1,0)
print('transposed random tensor:\n',transposedRandTens)

mult=torch.matmul(tensor,transposedRandTens)
print('\nmultiplying the two tensors:')
print(mult)