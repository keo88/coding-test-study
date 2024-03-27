import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
mp = []
alive = set()
for r in range(N):
    m_row = []
    damage = list(map(int, sys.stdin.readline().split()))
    for col in range(M):
        m_row.append([damage[col], 1, -r - col, -col])
        if damage[col] != 0:
            alive.add((r, col))
    mp.append(m_row)
a_bonus = N + M
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d8x = [0, 1, 0, -1, 1, 1, -1, -1]
d8y = [1, 0, -1, 0, 1, -1, 1, -1]


def select():
    if len(alive) <= 1:
        return None

    weak, strong = None, None
    weak_pos, strong_pos = (-1, -1), (-1, -1)
    for pos in alive:
        p_x, p_y = pos
        p_arr = mp[p_x][p_y]
        if not weak or p_arr < weak:
            weak = p_arr
            weak_pos = pos
        if not strong or p_arr > strong:
            strong = p_arr
            strong_pos = pos
    mp[weak_pos[0]][weak_pos[1]][0] += a_bonus

    return weak_pos, strong_pos


def get_laser_targets(attack: tuple[int, int], target: tuple[int, int]):
    visited = {}
    dq = deque([(attack, 0, (-1, -1))])
    ans = []

    while dq:
        pos, depth, frm = dq.popleft()
        if pos in visited:
            continue
        visited[pos] = depth, frm

        if pos == target:
            n_target = target
            while n_target != attack:
                ans.append(n_target)
                _, t_frm = visited[n_target]
                n_target = t_frm
            break

        p_x, p_y = pos
        for d in range(4):
            n_x, n_y = (p_x + dx[d]) % N, (p_y + dy[d]) % M
            n_pos = (n_x, n_y)
            if n_pos in visited or n_pos not in alive:
                continue
            dq.append((n_pos, depth + 1, pos))
    return ans


def get_bombard_targets(attack: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    ans = [target]
    t_x, t_y = target

    for d in range(8):
        n_x, n_y = (t_x + d8x[d]) % N, (t_y + d8y[d]) % M
        n_pos = (n_x, n_y)
        if n_pos == attack or n_pos not in alive:
            continue
        ans.append(n_pos)
    return ans


def print_mp():
    for row in range(N):
        print(' '.join(map(lambda x: str(x[0]), mp[row])))
    print()


for t in range(K):

    # print('t', t)
    # print_mp()

    select_res = select()
    if not select_res:
        break

    # print('selected', t)
    # print_mp()

    attacker_pos, target_pos = select_res
    ap_x, ap_y = attacker_pos

    deal = mp[ap_x][ap_y][0]
    mp[ap_x][ap_y][1] = -t

    attack_targets = get_laser_targets(attacker_pos, target_pos)
    if not attack_targets:
        attack_targets = get_bombard_targets(attacker_pos, target_pos)

    for i, at in enumerate(attack_targets):
        at_x, at_y = at
        health = mp[at_x][at_y][0]

        if i == 0:
            health -= deal
        else:
            health -= deal // 2
        if health <= 0:
            mp[at_x][at_y][0] = 0
            alive.remove(at)
        else:
            mp[at_x][at_y][0] = health

    involved = set(attack_targets)
    involved.add(attacker_pos)
    for survived in alive:
        if survived in involved:
            continue
        s_x, s_y = survived
        mp[s_x][s_y][0] += 1

last_res = select()
if not last_res:
    c_x, c_y = list(alive)[0]
else:
    _, l_str = last_res
    c_x, c_y = l_str
print(mp[c_x][c_y][0])

# a = [1, 2, 3, 4]
# b = [2, 2, 3, 4]
# k = a < b
# print('a < b ', a < b, 'a > b', a > b, 'a == b', a == b)