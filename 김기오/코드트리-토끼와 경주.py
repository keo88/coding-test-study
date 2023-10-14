from heapq import heappop, heappush
import sys

Q = int(input())
first_q = list(map(int, sys.stdin.readline().split()))
N, M, P = first_q[1], first_q[2], first_q[3]
dist, score = {}, {}
rhq = []
for i in range(P):
    pid = first_q[4 + 2 * i]
    d = first_q[5 + 2 * i]
    dist[pid] = d
    score[pid] = 0
    heappush(rhq, (0, 0, 0, 0, pid))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def move(cur: int, dist: int, l: int):
    dt = l - 1
    rt = dt * 2
    dist = dist % rt
    pos = []
    edge_dist = dt - cur
    pos.append(abs(dt - abs(dist - edge_dist)))
    edge_dist = cur

    abs_cur = abs(dist - edge_dist)
    if abs_cur > dt:
        abs_cur = rt - abs_cur
    pos.append(abs_cur)
    return pos


for q in range(1, Q - 1):
    commands = list(map(int, sys.stdin.readline().split()))

    if commands[0] == 200:
        K, S = commands[1], commands[2]
        picked_id = set()

        for k in range(K):
            acc, _, t_x, t_y, t_id = heappop(rhq)
            picked_id.add(t_id)
            t_dist = dist[t_id]
            n_poses = []
            for n_x in move(t_x, t_dist, N):
                heappush(n_poses, (n_x + t_y, n_x, t_y))
            for n_y in move(t_y, t_dist, M):
                heappush(n_poses, (t_x + n_y, t_x, n_y))
            _, f_x, f_y = heappop(n_poses)
            heappush(rhq, (acc + 1, f_x + f_y, f_x, f_y, t_id))

            for key in score:
                if key == t_id:
                    continue
                score[key] += f_x + f_y



