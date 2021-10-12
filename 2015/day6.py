import re


with open("inp6.txt") as file:
    data = file.read()


lights1 = [[0] * 1000 for _ in range(1000)]
lights2 = [[0] * 1000 for _ in range(1000)]


def turn_on1(x, y):
    lights1[y][x] = 1

def turn_off1(x, y):
    lights1[y][x] = 0

def toggle1(x, y):
    lights1[y][x] ^= 1

def turn_on2(x, y):
    lights2[y][x] += 1

def turn_off2(x, y):
    if lights2[y][x] > 0:
        lights2[y][x] -= 1

def toggle2(x, y):
    lights2[y][x] += 2


for line in data.splitlines():
    if 'toggle' in line:
        switch1 = toggle1
        switch2 = toggle2
    elif 'turn on' in line:
        switch1 = turn_on1
        switch2 = turn_on2
    else:
        switch1 = turn_off1
        switch2 = turn_off2

    x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            switch1(x, y)
            switch2(x, y)


lights_on_cnt = sum(1 for x in range(1000) for y in range(1000) if lights1[y][x] == 1)
print(lights_on_cnt)
assert 569999 == lights_on_cnt


total_brightness = sum(sum(row) for row in lights2)
print(total_brightness)
assert 17836115 == total_brightness
