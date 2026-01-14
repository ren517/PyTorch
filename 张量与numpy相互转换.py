import torch
import numpy as np

def dm01():
    t1 = torch.tensor([1,2,3])

    n1 = t1.numpy()
    print(f't1:{t1}{type(t1)}')
    print(f'n1:{n1}{type(n1)}')
    n1[0] = 100
    print(f't1:{t1}{type(t1)}')
    print(f'n1:{n1}{type(n1)}')

    n2 = t1.numpy().copy()
    print(f't1:{t1}{type(t1)}')
    print(f'n2:{n2}{type(n2)}')
    n2[0] = 1

    print(f't1:{t1}{type(t1)}')
    print(f'n2:{n2}{type(n2)}')

def dm02():
    n1 = np.array([11,22,33])
    t1 = torch.from_numpy(n1)
    t2 = torch.tensor(n1)

    print(f'n1: {n1} : {type(n1)}')
    print(f't1 : {t1} : {type(t1)}')
    print(f't2 : {t2} : {type(t2)}')
    t1[0] = 100
    print(f'n1: {n1} : {type(n1)}')
    print(f't1 : {t1} : {type(t1)}')
    print(f't2 : {t2} : {type(t2)}')

def dm03():
    t1 = torch.tensor(100)
    value = t1.item()
    print(f'{t1}, {value}')

if __name__ == '__main__':
    #dm01()
    #dm02()
    dm03()