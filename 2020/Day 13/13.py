with open('input.txt') as file:
    data = file.read()


data = data.splitlines()

depart_timestamp = int(data[0])
ids = []
for v in data[1].split(","):
    if v.isdigit():
        v = int(v)
    ids.append(v)

time_to_wait = 9999999999999999999
best_id = 0

for id in ids:
    if id == 'x':
        continue

    # print(f"ID:{id}, {depart_timestamp % id}, time to wait: {id - (depart_timestamp % id)}")
    temp = id - depart_timestamp % id
    if temp < time_to_wait:
        time_to_wait = temp
        best_id = id

# part1
print(time_to_wait, time_to_wait * best_id)



from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

a = [id for id in ids if id != 'x']
n = [i for i in range(len(ids)) if ids[i] != 'x']

cr = chinese_remainder(a, n)
N = reduce(lambda x, y: x * y, a)

print(N % cr)