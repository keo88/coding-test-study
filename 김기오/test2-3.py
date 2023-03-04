from heapq import heappush, heappop

def solution(n, k, infos):
    spin_until = infos[0][0]
    req_walk = n // 2
    hq, result = [], []
    stop_time = 0

    for in_time, in_pos in infos:
        # print(f'in_time{in_time} ')
        stop_time = in_time - spin_until

        if stop_time < 0:
            #돌고 있는데 돌아옴. 다시 안돌림
            stop_time = 0
            while hq and hq[0] <= in_time :
                popped = heappop(hq)
                result.append(popped)
            heappush(hq, in_time + req_walk)
        else:
            #무조건 다시 돌리게 됨.
            # print(f' stop_time{stop_time} ')
            while hq:
                popped = heappop(hq)
                result.append(popped + stop_time)
                # print(f'popped {popped + stop_time} stop_time {stop_time}')
            result.append(in_time + req_walk)
            spin_until = in_time + k
            # print(f'spin_until {spin_until}')

    while hq:
        if hq[0] <= spin_until:
            result.append(heappop(hq))
        else:
            heappop(hq)
            result.append(-1)

    return result