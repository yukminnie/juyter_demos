from random import randint

data_a = [randint(-10,10) for _ in range(1,11)]
data_b = {x: randint(10,20) for x in range(1,11)}
data_c = {randint(-10,10) for _ in range(1,11)}

print("{}\n{}\n{}\n".format(data_a, data_b, data_c))

data_a_set = [x for x in data_a if x >= 0]

data_b_set = {k: v for k, v in data_b.items() if v >= 15}

data_c_set = {x for x in data_c if x % 2 == 0}

print("{}\n{}\n{}\n".format(data_a_set, data_b_set, data_c_set))
