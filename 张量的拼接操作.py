"""
cat() 不改变维度，拼接张量，除了拼接的那个维度外，其他维度数必须保持一致
stack() 会改变维度数，拼接张量，所有的维度都必须保持一致
"""

import torch

def dm01():
    t1 = torch.randint(1, 10, size=(2,3))
    print(f't1 : {t1}, shape: {t1.shape}')
    t2 = torch.randint(1, 10, size=(2,3))
    print(f't2 : {t2}, shape: {t2.shape}')

    t3 = torch.cat([t1, t2], dim=0)
    print(f't3 : {t3}, shape: {t3.shape}')

    t4 = torch.stack((t1, t2), dim=0)
    print(f't4 : {t4}, shape: {t4.shape}')
    t4 = torch.stack((t1, t2), dim=1)
    print(f't4 : {t4}, shape: {t4.shape}')
    t4 = torch.stack((t1, t2), dim=2)
    print(f't4 : {t4}, shape: {t4.shape}')



if __name__ == '__main__':
    dm01()