# range(10) == range(1,11)
# 集合可以去除相同元素
# 集合可以用生成式， 或者set(list)方法生成
# python 2 vs python 3  xrange:range iteritems:items
from random import randint

data_a = [randint(-10,10) for _ in range(1,11)]
data_b = {x: randint(10,20) for x in range(1,11)}
data_c = {randint(-10,10) for _ in range(1,11)}
data_d = set(data_a)

print("{}\n{}\n{}\n{}\n".format(data_a, data_b, data_c, data_d))

data_a_set = [x for x in data_a if x >= 0]

data_b_set = {k: v for k, v in data_b.items() if v >= 15}

data_c_set = {x for x in data_c if x % 2 == 0}

data_d_set = {x for x in data_d if x % 2 == 0}

print("{}\n{}\n{}\n{}".format(data_a_set, data_b_set, data_c_set, data_d_set))
