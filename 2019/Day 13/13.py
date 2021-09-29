from icc import ICC


ID_EMPTY = 0
ID_WALL = 1
ID_BLOCK = 2
ID_PADDLE = 3
ID_BALL = 4


def gen_output():
    out = []
    while True:
        r = icc.run()
        if r is None:
            return out
        out.append(r)


def play():
    data = []
    paddle_x, ball_x = 0, 0
    inp = 0
    max_score = 0
    while True:
        r = icc.run(inp)
        if r is None:
            return max_score
        data.append(r)
        if len(data) == 3:
            x, y, tid = data
            data = []
            if x == -1 and y == 0:
                max_score = max(tid, max_score)

            if tid == ID_PADDLE:
                paddle_x = x
            elif tid == ID_BALL:
                ball_x = x

            if paddle_x > ball_x:
                inp = -1
            elif paddle_x < ball_x:
                inp = 1
            else:
                inp = 0


with open("input.txt") as file:
    icc = ICC(file.read())

# part 1
ids = gen_output()[2::3]
print(ids.count(ID_BLOCK))

# part 2
icc.restart()
icc.intcode[0] = 2 # play for free
score = play()
print(score)