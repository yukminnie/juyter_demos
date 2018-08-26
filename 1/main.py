# **** 列表解析 分割线 ****
from random import randint

data = [randint(-10, 10) for _ in range(10)]
print(data)

# 第1种方法
# 迭代
data_a = []
for x in data:
    if x >= 0:
        data_a.append(x)
print(data_a)

# 第2种方法
# filter 函数
# filter(lambda x: x >= 0, data)

# 第3种方法
# 列表解析式
data_b = [x for x in data if x >= 0]
print(data_b)

# 计算运行时间 timeit函数
# 结果： 迭代(大于filter) filter(909ns) 列条解析(455ns)

# **** 字典解析 分割线 ****
from random import randint

data = {x: randint(60,100) for x in range(1,21)}
print(data)
data_a = {k: v for k, v in data.items() if v >= 90}
print(data_a)

# ****分割线****
from random import randint

one_data = [randint(-10, 10) for _ in range(10)]
two_data = {randint(-10, 10) for _ in range(10)}
three_data = set(one_data)
print(one_data)
print(two_data)
print(three_data)

two_data = {x for x in data if x % 2 == 0}
print(data_a)
