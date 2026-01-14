# torch.zeros(), full()
import torch
t1 = torch.ones(2, 3)
print(t1)

t2 = torch.tensor([[1, 2], [2, 3], [3, 4]])
print(t2)

t3 = torch.ones_like(t2)
print(t3)

t2 = t2.type(torch.float32)
print(t2)
