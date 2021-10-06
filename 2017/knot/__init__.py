from functools import reduce
from operator import xor

def knot_rounds(lens, rounds=64):
    skip = 0
    idx = 0
    table = list(range(256))

    for _ in range(rounds):
        for length in lens:
            rev = [table[(idx + i) % 256] for i in reversed(range(length))]
            for i, x in enumerate(rev):
                table[(idx + i) % 256] = x

            idx = idx + length + skip
            skip += 1

    return table

def knot_hash(data: str):
    lens = [ord(c) for c in data] + [17, 31, 73, 47, 23]
    sparse_hash = knot_rounds(lens)
    dense_hash = [reduce(xor, sparse_hash[i: i+16]) for i in range(0, 256, 16)]
    return ''.join('{:02x}'.format(x) for x in dense_hash)