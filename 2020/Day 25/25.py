MAGIC = 20201227

with open('input.txt') as file:
    data = file.read()

k1, k2 = map(int, data.splitlines())

def compute_loop_size(sn, key):
    loop_size = 0
    v = 1
    while v != key:
        loop_size += 1
        v = v * sn
        v = v % MAGIC
    return loop_size

def transform(sn, loop_size):
    v = 1
    for _ in range(loop_size):
        v = v * sn
        v = v % MAGIC
    return v

ls2 = compute_loop_size(7, k2)
enc = transform(k1, ls2)

print(f"Encryption key: {enc}")