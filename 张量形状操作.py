"""
reshape()
unsqueeze()
squeeze()
transpose()
permute()
vier()
contiguous()
is_contiguous()

*** reshape()
*** unsqueeze()
*** permute()
*** view()
"""
import torch
from click import echo


def dm01():
    torch.manual_seed(222)
    t1 = torch.randint(low=0, high=10, size=(2,3))
    print(f't1 : {t1}: {t1.shape[0]}')

def dm02():
    torch.manual_seed(222)
    t1 = torch.randint(low=0, high=10, size=(2,3))
    print(f't1 : {t1}, shape: {t1.shape}')

    # 在0维上添加一维
    t2 = t1.unsqueeze(0)# 1,2,3
    print(f't2 : {t2}, shape: {t2.shape}')

    # 在1维上添加一维
    t3 = t1.unsqueeze(1)# 2, 1, 3
    print(f't3 : {t3}, shape: {t3.shape}')
    
    # 在2维上添加一维
    t4 = t1.unsqueeze(2)# 2, 3, 1
    print(f't4 : {t4}, shape: {t4.shape}')

    # 删除所有为1的维度
    t6 = torch.randint(1, 10, size=(2, 1, 3, 1, 1))
    print(f't6 : {t6}, shape: {t6.shape}')

    t6.squeeze_()
    print(f't6 : {t6}, shape: {t6.shape}')

def dm03():
    # t1 = torch.ones(2, 3, dtype=torch.int)
    # print(f't1 : {t1}, shape: {t1.shape}')
    torch.manual_seed(222)
    t1 = torch.randint(low=0, high=10, size=(2, 3, 4))
    print(f't1 : {t1}, shape: {t1.shape}')
    t2 = t1.transpose(1, 2)
    print(f't1 : {t1}, shape: {t1.shape}')
    print(f't2 : {t2}, shape: {t2.shape}')

    # 把（2， 3， 4） 改成（4， 2， 3）
    t3 = t1.permute(2, 0, 1)
    print(f't3 : {t3}, shape: {t3.shape}')

    # view() 当用permute 和 transpose后不能用view()
    # view()只能修改连续的张量， 内存存储顺序等于张量中现实的顺序
    print(t3.is_contiguous())
    print(t1.is_contiguous())
    t4 = t3.contiguous()
    print(f't4 : {t4}, shape: {t4.shape}')
    print(t4.is_contiguous())

    t4 = torch.randint(low=0, high=10, size=(2, 3))
    print(f't4 : {t4}, shape: {t4.shape}')
    print(t4.is_contiguous())

    t5 = t4.view(3, 2)
    print(f't5 : {t5}, shape: {t5.shape}')
    print(t5.is_contiguous())


if __name__ == '__main__':
    # dm01()
    # dm02()
    dm03()