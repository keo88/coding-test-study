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
intMax = 2 ** 31 - 1
intMin = - 2**31


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
    # print(score)

    if commands[0] == 200:
        K, S = commands[1], commands[2]
        picked_score = {}
        picked_info = {}
        tot_k_score = 0

        for k in range(K):
            acc, _, t_x, t_y, t_id = heappop(rhq)
            t_dist = dist[t_id]
            n_poses = []
            for n_x in move(t_x, t_dist, N):
                heappush(n_poses, (-n_x - t_y, -n_x, -t_y))
            for n_y in move(t_y, t_dist, M):
                heappush(n_poses, (-t_x - n_y, -t_x, -n_y))
            _, f_x, f_y = heappop(n_poses)
            f_x, f_y = -f_x, -f_y
            # print('k', k, t_id, 'f_x', 'f_y', f_x, f_y, f_x + f_y + 2)
            t_score = f_x + f_y + 2
            tot_k_score += t_score
            picked_info[t_id] = (t_score, f_x, f_y)
            if t_id not in picked_score:
                picked_score[t_id] = t_score
            else:
                picked_score[t_id] += t_score
            heappush(rhq, (acc + 1, t_score, f_x, f_y, t_id))
            # print('k round', k, picked_score, tot_k_score)

        for key in score:
            if key in picked_score:
                score[key] += tot_k_score - picked_score[key]
            else:
                score[key] += tot_k_score

        best_key = None
        best_value = (intMin, intMin, intMin)
        for key in picked_info:
            if not best_key or picked_info[key] > best_value:
                best_value = picked_info[key]
                best_key = key
        score[best_key] += S

    elif commands[0] == 300:
        pid, L = commands[1], commands[2]
        dist[pid] *= L

# print(score)
best_key = None
best_score = intMin
for key in score:
    if not best_key or best_score < score[key]:
        best_score = score[key]
        best_key = key
print(best_score)