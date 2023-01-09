import sys
from itertools import permutations


innings_count = int(sys.stdin.readline())
innings_record = list()
for i in range(innings_count):
    inning_record = list(map(int, sys.stdin.readline().split()))
    innings_record.append(inning_record)
player_scores = list(zip(*innings_record))
max_score = 0


def get_score(player_order: list):
    score = 0
    current_player = 0

    for inning in range(innings_count):

        outs = 0
        b1, b2, b3 = 0, 0, 0

        while outs < 3:

            player_hit = player_scores[player_order[current_player]][inning]

            if player_hit == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            elif player_hit == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif player_hit == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif player_hit == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            else:
                outs += 1

            current_player = (current_player + 1) % 9
    return score


for perm in permutations(range(1, 9)):
    lineups = list(perm[:3]) + [0] + list(perm[3:])
    max_score = max(get_score(lineups), max_score)
print(max_score)
