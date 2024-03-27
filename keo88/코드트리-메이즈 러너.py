import sys

N, M, K = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
humans = {}

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    humans[i] = (x - 1, y - 1)
x, y = map(int, sys.stdin.readline().split())
miro[x - 1][y - 1] = -2
out = (x - 1, y - 1)
totalDist = 0
maxInt = 2 ** 31 - 1


def movePlayers():
    global totalDist
    outX, outY = out
    removals, edits = [], []
    for i in humans:
        possiblePoses = []
        human = humans[i]
        hX, hY = human
        if outX - hX > 0:
            possiblePoses.append((hX + 1, hY))
        elif outX - hX < 0:
            possiblePoses.append((hX - 1, hY))
        if outY - hY > 0:
            possiblePoses.append((hX, hY + 1))
        elif outY - hY < 0:
            possiblePoses.append((hX, hY - 1))
        for pos in possiblePoses:
            pos_x, pos_y = pos
            if miro[pos_x][pos_y] > 0:
                continue
            elif miro[pos_x][pos_y] <= 0:
                totalDist += 1
                edits.append((i, (pos_x, pos_y)))
                if miro[pos_x][pos_y] == -2:
                    removals.append(i)
                break

    for edit in edits:
        i, pos = edit
        humans[i] = pos
    for removal in removals:
        del humans[removal]


def getRect(human, out):
    min_hx, min_hy = human
    s_x, s_y = min(min_hx, out[0]), min(min_hy, out[1])
    b_x, b_y = max(min_hx, out[0]), max(min_hy, out[1])
    surp_x, surp_y = 0, 0
    x_diff, y_diff = b_x - s_x, b_y - s_y
    l = x_diff
    if x_diff > y_diff:
        l = x_diff
        surp_y = x_diff - y_diff
    elif x_diff < y_diff:
        l = y_diff
        surp_x = y_diff - x_diff
    t_x = max(0, s_x - surp_x)
    t_y = max(0, s_y - surp_y)

    return (t_x, t_y, l)


def rotate():
    global out
    min_ind = -1
    min_dist = maxInt
    t_x, t_y, l = maxInt, maxInt, maxInt
    for i in humans:
        human = humans[i]
        dist = max(abs(out[0] - human[0]), abs(out[1] - human[1]))
        if dist < min_dist:
            min_ind = i
            min_dist = dist
            t_x, t_y, l = getRect(humans[i], out)
        elif dist == min_dist:
            candidate = humans[min_ind]
            n_t_x, n_t_y, n_l = getRect(human, out)
            if t_x > n_t_x:
                min_ind = i
                min_dist = dist
                t_x, t_y, l = n_t_x, n_t_y, n_l
            elif t_x == n_t_x:
                if t_y > n_t_y:
                    min_ind = i
                    min_dist = dist
                    t_x, t_y, l = n_t_x, n_t_y, n_l
    cent = l / 2
    c_x = t_x + l/2
    c_y = t_y + l/2
    tb_x = t_x + l
    tb_y = t_y + l

    patch = []
    for i in range(l + 1):
        patch.append([0] * (l + 1))
    for i in range(l + 1):
        for j in range(l + 1):
            dx, dy = cent - i, cent - j
            value = miro[t_x + i][t_y + j]

            if value > 0:
                value -= 1
            patch[round(cent - dy)][round(cent + dx)] = value

    for i in range(l + 1):
        for j in range(l + 1):
            miro[t_x + i][t_y + j] = patch[i][j]
            if patch[i][j] == -2:
                out = (t_x + i, t_y + j)
    for i in humans:
        h_x, h_y = humans[i]
        if t_x <= h_x <= tb_x and t_y <= h_y <= tb_y:
            dx, dy = c_x - h_x, c_y - h_y
            humans[i] = (round(c_x - dy), round(c_y + dx))


k = K
while k:
    movePlayers()
    if len(humans) == 0:
        break
    rotate()
    k -= 1

print(totalDist)
print(out[0] + 1, out[1] + 1)
