import torch
import torch.nn as nn
data = torch.Tensor([1,2,3])
softmax_function = nn.Softmax(dim = 0)
output = softmax_function(data)

class MySoftmax(nn.Module):
  def __init__(self):
    super().__init__()

  def forward(self, x):
    x_exp = torch.exp(x)
    total = x_exp.sum(0, keepdims= True)
    return x_exp/total

my_softmax = MySoftmax()
output = my_softmax(data)
assert round ( output [0]. item () , 2) == 0.0
print(output)

class StableMySoftmax(nn.Module):
  def __init__(self):
    super().__init__()

  def forward(self, x):
    c = torch.max(x, dim=0)
    x_exp = torch.exp(x - c.values)
    total = x_exp.sum(0, keepdims= True)
    return x_exp/total

stable_softmax = StableMySoftmax()
output = stable_softmax(data)
print(output)
