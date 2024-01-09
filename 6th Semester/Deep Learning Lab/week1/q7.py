import torch

print(torch.cuda.is_available())

tens1=torch.rand(size=(2,3))
print('tensor 1:\n',tens1)
print('device of tens1: ',tens1.device)
tens1_on_gpu=tens1.cuda()
print('device of tens1 after transfer: ',tens1_on_gpu.device)

tens2=torch.rand(size=(2,3))
print('\ntensor 2:\n',tens2)
print('device of tens2: ',tens2.device)
tens2_on_gpu=tens2.cuda()
print('device of tens2 after transfer: ',tens2_on_gpu.device)
