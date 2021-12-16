import pytest
from day16 import parse_packet, hex_to_bin, get_version_sum, set_version_sum


@pytest.fixture
def file_data():
    with open("inp16.txt") as file:
        return file.read()


def run(data):
    binary = hex_to_bin(data)
    return parse_packet(binary)[1]


def check_result(data, expected):
    result = run(data)
    assert len(result) == 1
    assert result[0] == expected


def test_version_sum():
    set_version_sum(0)
    run("8A004A801A8002F478")
    assert get_version_sum() == 16

    set_version_sum(0)
    run("620080001611562C8802118E34")
    assert get_version_sum() == 12

    set_version_sum(0)
    run("C0015000016115A2E0802F182340")
    assert get_version_sum() == 23

    set_version_sum(0)
    run("A0016C880162017C3686B18A3D4780")
    assert get_version_sum() == 31


def test_basic_value():
    check_result("D2FE28", 2021)


def test_sum():
    check_result("C200B40A82", 3)


def test_product():
    check_result("04005AC33890", 54)


def test_minimum():
    check_result("880086C3E88112", 7)


def test_maximum():
    check_result("CE00C43D881120", 9)


def test_less_than():
    check_result("D8005AC2A8F0", 1)


def test_greater_than():
    check_result("F600BC2D8F", 0)


def test_equal():
    check_result("9C005AC2F8F0", 0)


def test_complex_expression():
    check_result("9C0141080250320F1802104A08", 1)


def test_part1(file_data):
    set_version_sum(0)
    run(file_data)
    assert get_version_sum() == 967


def test_part_2(file_data):
    check_result(file_data, 12883091136209)


pytest.main()
