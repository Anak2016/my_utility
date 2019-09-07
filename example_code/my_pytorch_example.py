
#------Refactor using Dataset
import torch
x_train, y_train = (torch.randn(3,6),torch.randn(3,6))
bs =  32 # batch size
start_i = 0
end_i = 32
from torch.utils.data import TensorDataset
train_ds = TensorDataset(x_train, y_train)
xb = x_train[start_i:end_i]
yb = y_train[start_i:end_i]

xb1,yb1 = train_ds[start_i:end_i]
assert (torch.equal(xb, xb1)and torch.equal(yb,yb1)), "not euqal in value"

#----loop through n with bs batches
import torch
x_train, y_train = (torch.randn(100,5),torch.randn(3,6))
bs =  32 # batch size
start_i = 0
end_i = 32
n = 105
for i in range((n-1)//bs+1):
    xb = x_train[i*bs : i*bs+bs]
    print(xb.shape)

# ====================
# ==Pytorch Model structure example
# ====================
#----get_data
from torch.utils.data import DataLoader
def get_data(train_ds, valid_ds, bs):
    return (
        DataLoader(train_ds, batch_size=bs, shuffle=True),
        DataLoader(valid_ds, batch_size=bs * 2),
    )
#----loss_batch
def loss_batch(model, loss_func, xb, yb, opt=None):
    loss = loss_func(model(xb), yb)

    if opt is not None:
        loss.backward()
        opt.step()
        opt.zero_grad()

    return loss.item(), len(xb)

#----fit pytorch
import numpy as np

def fit(epochs, model, loss_func, opt, train_dl, valid_dl):
    for epoch in range(epochs):
        model.train()
        for xb, yb in train_dl:
            loss_batch(model, loss_func, xb, yb, opt)

        model.eval()

        with torch.no_grad():
            losses, nums = zip(
                *[loss_batch(model, loss_func, xb, yb) for xb, yb in valid_dl]
            )
        val_loss = np.sum(np.multiply(losses, nums)) / np.sum(nums)

        print(epoch, val_loss)
#------model python
import torch.nn as nn
import torch.nn.functional as F
class Mnist_CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=2, padding=1)
        self.conv2 = nn.Conv2d(16, 16, kernel_size=3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(16, 10, kernel_size=3, stride=2, padding=1)

    def forward(self, xb):
        xb = xb.view(-1, 1, 28, 28)
        xb = F.relu(self.conv1(xb))
        xb = F.relu(self.conv2(xb))
        xb = F.relu(self.conv3(xb))
        xb = F.avg_pool2d(xb, 4)
        return xb.view(-1, xb.size(1))

lr = 0.1

#----run model pytorch
# train_dl, valid_dl = get_data(train_ds, valid_ds, bs)
# model, opt = get_model()
# fit(epochs, model, loss_func, opt, train_dl, valid_dl)

#----Sequential pytorch
def preprocess(x):
    return x.view(-1, 1, 28, 28)
model = nn.Sequential(
    Lambda(preprocess),
    nn.Conv2d(1, 16, kernel_size=3, stride=2, padding=1),
    nn.ReLU(),
    nn.Conv2d(16, 16, kernel_size=3, stride=2, padding=1),
    nn.ReLU(),
    nn.Conv2d(16, 10, kernel_size=3, stride=2, padding=1),
    nn.ReLU(),
    nn.AvgPool2d(4),
    Lambda(lambda x: x.view(x.size(0), -1)),
)