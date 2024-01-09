import torch
import numpy as np

np_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('numpy array:\n',np_array)

np_to_tensor=torch.from_numpy(np_array)
print('torch tensor:\n',np_to_tensor)

back_to_np=np_to_tensor.numpy()
print('back to numpy:\n',back_to_np)