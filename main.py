import torch
import numpy as np
"""
张量的基本创建方式：
    torch.tensor 根据指定的数据创建张量
    torch.Tensor 根据形状创建张量，也可以创建指定数据的张量
    torch.IntTensor, torch,FloatTensor, torch.DoubleTensor 创建指定类型张量
"""
def dm01():
    t1 = torch.tensor(10)
    print(f't1 : {t1} : {type(t1)}')
    print('-' * 30)

    data = [[1, 2, 3], [4, 5, 6]]
    t2 = torch.tensor(data)
    print(f't2 : {t2} : {type(t2)}')
    print('-' * 30)

    arr1 = np.array([[1, 2, 3], [2, 3,4]])
    t3 = torch.tensor(arr1, dtype = torch.float) # torch.Tensor不支持这个操作
    print(f't3 : {t3} : {type(t3)}')

    arr2 = np.random.randint(0, 10, size = (3, 5))
    t4 = torch.tensor(arr2)
    print(f't4 : {t4} : {type(t4)}')

    t5 = torch.Tensor(2, 3)
    print(f't5 : {t5}, {type(t5)}')

def dm02():
    t1 = torch.IntTensor(10)
    print(f't1 : {t1} : {type(t1)}')
    print('-' * 30)

    data = [[1, 2, 3], [4, 5, 6]]
    t2 = torch.IntTensor(data)
    print(f't2 : {t2} : {type(t2)}')
    print('-' * 30)

    arr1 = np.array([[1, 2, 3], [2, 3, 4]])
    t3 = torch.IntTensor(arr1)  # torch.Tensor不支持这个操作
    print(f't3 : {t3} : {type(t3)}')

    arr2 = np.random.randint(0, 10, size=(3, 5))
    t4 = torch.IntTensor(arr2)
    print(f't4 : {t4} : {type(t4)}')

    t5 = torch.IntTensor(2, 3)
    print(f't5 : {t5}, {type(t5)}')
if __name__ == '__main__':
    # dm01()
    dm02()