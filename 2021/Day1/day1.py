with open("inp1.txt") as file:
    data = file.read()

depths = [int(line) for line in data.splitlines()]
depth_inc_cnt = 0


for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        depth_inc_cnt += 1

print(f"Part 1: {depth_inc_cnt}")
assert depth_inc_cnt == 1832


depth_windowed_inc_cnt = 0
for i in range(1, len(depths) - 2):
    if sum(depths[i: i + 3]) > sum(depths[i - 1: i + 2]):
        depth_windowed_inc_cnt += 1

print(f"Part 2: {depth_windowed_inc_cnt}")
assert depth_windowed_inc_cnt == 1858
