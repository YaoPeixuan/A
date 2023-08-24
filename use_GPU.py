import torch
import torch.cuda

print(torch.cuda.is_available())
# print()
torch.zeros(1).cuda()