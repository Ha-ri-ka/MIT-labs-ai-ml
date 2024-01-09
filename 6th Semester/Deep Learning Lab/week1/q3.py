import torch
tens=torch.tensor([[1,2,3],[4,5,6]])
print(tens)
for i in range (2):
    for j in range(3):
        ele=tens[i,j]
        print(f'tens[{i}][{j}]={ele}')