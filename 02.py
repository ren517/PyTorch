import torch

def dm01():
    t1 = torch.arange(0, 10, 2)
    print(t1)
    print('-' * 30)

    # 等差数列
    t2 = torch.linspace(0, 10, steps=5)
    print(t2)

    torch.manual_seed(999)
    t1 = torch.rand(size = (2, 3))
    print(t1)

    t2 = torch.randn(size = (2,3))
    print(t2)

    t3 = torch.randint(low = 0, high=10, size=(3, 5))
    print(t3)

if __name__ == '__main__':
    dm01()