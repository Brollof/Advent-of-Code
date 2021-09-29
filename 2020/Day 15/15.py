
starting = [9,3,1,0,8,4]

def run(limit):
    nums = {n: (turn, turn) for turn, n in enumerate(starting, 1)}
    turns = len(starting)
    last_n = starting[-1]

    while turns < limit:
        turns += 1
        n = nums[last_n][0] - nums[last_n][1]

        if n in nums:
            nums[n] = (turns, nums[n][0])
        else:
            nums[n] = (turns, turns)

        last_n = n
    return last_n


# part 1
print(run(2020))

# part 2
print(run(30_000_000))
