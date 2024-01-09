import torch

tens=torch.tensor([[1,2,3],[4,5,6]])
print('original tensor:\n',tens)

#reshape
print('\nreshaped tensor:',torch.reshape(tens,(1,6)))

#view
view_tens=tens.view_as(tens)
print('\nView of original tensor:\n',view_tens)

#stack
print('\nStacking')
tens1=torch.tensor([1,2,3])
tens2=torch.tensor([4,5,6])
print(f'tens1:{tens1}\ntens2:{tens2}')
stacked=torch.stack([tens2,tens1])
print('tens2 upon tens1:\n',stacked)
stacked=torch.stack([tens1,tens2])
print('tens1 upon tens2:\n',stacked)

print('\nSqueezing')
x = torch.ones(size=(1, 3, 1, 4),dtype=int)
squeezed_tensor = torch.squeeze(x)
print("Original Tensor:")
print(x)
print("Squeezed Tensor:")
print(squeezed_tensor)

print('\nUnsqueezing')
print("Squeezed Tensor:")
print(squeezed_tensor)
unsqueezed_tensor = torch.unsqueeze(x, dim=0)
print("Unsqueezing Tensor by adding singleton dimension at index 0:")
print(unsqueezed_tensor)
