import torch
import torch.nn as nn
from torchvision.transforms import transforms
from torch.utils.data import Dataset, DataLoader, random_split

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
class CNNClassifier(nn.Module):
    def __init__(self):
        super(CNNClassifier, self).__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, stride=2, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=0),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 4, kernel_size=3, stride=2, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.classification_head = nn.Sequential(
            nn.Linear(4, 20),
            nn.ReLU(),
            nn.Linear(20, 2)
        )

    def forward(self, x):
        features = self.net(x)
        features = features.view(features.size(0), -1)
        return self.classification_head(features)

def generateGaussian(tindx):
    return torch.normal(tindx[0], tindx[1], (1, 42, 42))

class MyDataSet(Dataset):
    def __init__(self, n):
        classes = {0: (0.5, 2), 1: (1, 2.5)}
        self.y = [torch.round(torch.rand(1))[0].long() for _ in range(n)]
        self.X = [generateGaussian(classes[self.y[i].item()]) for i in range(n)]

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

    def __len__(self):
        return len(self.X)

model = CNNClassifier()
model.to(device)  # Move model to GPU if available
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
batch_size = 4

dataset = MyDataSet(1200)
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_size = 1000
test_size = 200
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
# train_dataset, test_dataset = (dataset, [train_size, test_size])
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

total_params = sum(p.numel() for p in model.parameters())

print('total params: ', total_params)

for epoch in range(6):
    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        inputs, labels = data[0].to(device), data[1].to(device)

        optimizer.zero_grad()

        outputs = model(inputs)
        loss = loss_fn(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 100 == 99:
            print('[%d, %5d] loss: %.3f' % (epoch + 1, i + 1, running_loss / 100))
            running_loss = 0.0

print(f"Finished Training. Final loss = {loss.item()}, Total params = {total_params}")

correct, total = 0, 0

for i, vdata in enumerate(test_loader):
    tinputs, tlabels = vdata[0].to(device), vdata[1].to(device)
    toutputs = model(tinputs)

    _, predicted = torch.max(toutputs, 1)
    total += tlabels.size(0)
    correct += (predicted == tlabels).sum()


print(f"Correct = {correct}, Total = {total}")
print(f"Accuracy = {100.0 * correct/total}")