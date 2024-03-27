import sys
from collections import deque


def bfs():
    liable_parties = list(range(parties_cnt))
    q = deque(detectors)
    already_processed = []
    while q:
        detector = q.popleft()
        already_processed.append(detector)
        detector_parties = player_parties_dict[detector]
        for party in detector_parties:
            if party in liable_parties:
                liable_parties.remove(party)
            participants = filter(lambda x: x not in already_processed, parties[party])
            q.extend(participants)

    return len(liable_parties)


N, parties_cnt = map(int, sys.stdin.readline().split())
detectors = list(map(int, sys.stdin.readline().split()))[1:]

parties = []
player_parties_dict = dict()
for i in range(1, N + 1):
    player_parties_dict[i] = []
for i in range(parties_cnt):
    parties.append(list(map(int, sys.stdin.readline().split()))[1:])
    for player in parties[i]:
        player_parties_dict[player].append(i)

print(bfs())
