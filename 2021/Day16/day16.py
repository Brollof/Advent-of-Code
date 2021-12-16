from operator import mul, lt, gt, eq
from functools import reduce
from enum import IntEnum


class OPS(IntEnum):
    SUM = 0
    PROD = 1
    MIN = 2
    MAX = 3
    VAL = 4
    GT = 5
    LT = 6
    EQ = 7


version_sum = 0


def hex_to_bin(h: str) -> str:
    return ''.join(f"{int(c, base=16):04b}" for c in h)


def get_version_sum():
    return version_sum


def set_version_sum(value):
    global version_sum
    version_sum = value


def parse_packet(packet):
    global version_sum
    packet_version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)

    version_sum += packet_version
    packet = packet[6:]
    total_consumed = 6
    values = []

    if type_id == OPS.VAL:
        value = ''
        while True:
            total_consumed += 5
            value += packet[1:5]
            if packet[0] == '0':  # Last packet
                values.append(int(value, 2))
                break
            packet = packet[5:]
    else:  # Operator
        length_type_id = packet[0]
        packet = packet[1:]
        total_consumed += 1

        if length_type_id == '0':
            total_length = int(packet[:15], 2)
            packet = packet[15:]
            total_consumed += 15
            while total_length > 0:
                consumed, v = parse_packet(packet)
                values.extend(v)
                total_consumed += consumed
                total_length -= consumed
                packet = packet[consumed:]
        else:
            sub_packets_num = int(packet[:11], 2)
            packet = packet[11:]
            total_consumed += 11
            for _ in range(sub_packets_num):
                consumed, v = parse_packet(packet)
                values.extend(v)
                packet = packet[consumed:]
                total_consumed += consumed

    match type_id:
        case OPS.SUM: values = [sum(values)]
        case OPS.PROD: values = [reduce(mul, values)]
        case OPS.MIN: values = [min(values)]
        case OPS.MAX: values = [max(values)]
        case OPS.LT: values = [lt(*values)]
        case OPS.GT: values = [gt(*values)]
        case OPS.EQ: values = [eq(*values)]

    return total_consumed, values


if __name__ == '__main__':
    with open("inp16.txt") as file:
        data = file.read()

    binary = hex_to_bin(data)
    _, result = parse_packet(binary)
    p2 = result[0]

    print(f"Part 1: {version_sum}")
    assert version_sum == 967

    print(f"Part 2: {p2}")
    assert p2 == 12883091136209
