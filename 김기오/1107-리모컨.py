import sys


def get_score(candidate: int):
    digits_count = len(str(candidate))
    return digits_count + abs(N - candidate)


def dfs(cur_filled_digits: int, acc_number: int):
    candidates = []
    filled_num = cur_filled_digits
    if filled_num == digits_length:
        return acc_number
    zeros = digits_length - filled_num - 1
    multiple_value = 10 ** zeros
    target = digits[filled_num]
    closest_big = next((x for x in usable_buttons if x > target), None)
    closest_small = next((x for x in rev_usable_buttons if x < target), None)

    if closest_big is not None:
        bigger_num = acc_number + int(str(closest_big) + str(least_button) * zeros)
        candidates.append(bigger_num)
    else:
        if filled_num == 0:
            if least_nonzero != -1:
                bigger_num = int(str(least_nonzero) + str(least_button) * (zeros + 1))
                candidates.append(bigger_num)
    if closest_small is not None:
        smaller_num = acc_number + int(str(closest_small) + str(last_button) * zeros)
        candidates.append(smaller_num)
    else:
        if filled_num == 0:
            if last_button != 0 and zeros != 0:
                smaller_num = int(str(last_button) * zeros)
                candidates.append(smaller_num)

    if target in usable_buttons:
        candidates.append(dfs(filled_num + 1, acc_number + multiple_value * target))

    if len(candidates) == 0:
        return 0
    else:
        scores = list(map(get_score, candidates))
        i = scores.index(min(scores))
        return candidates[i]


def get_closest_number():
    use_digits_button_case = dfs(0, 0)
    make_use_of_start_case = abs(100 - N)

    return min(get_score(use_digits_button_case), make_use_of_start_case)


N = int(input())
mal_cnt = int(input())
if mal_cnt > 0:
    mal_buttons = list(map(int, sys.stdin.readline().split()))
else:
    mal_buttons = []
digits = list(map(int, list(str(N))))
digits_length = len(digits)


usable_buttons = list(range(10))
for mal_button in mal_buttons:
    usable_buttons.remove(mal_button)

if len(usable_buttons) == 0:
    print(abs(100 - N))
else:
    usable_buttons.sort()
    rev_usable_buttons = list(reversed(usable_buttons))
    least_button, last_button = usable_buttons[0], usable_buttons[-1]
    if least_button == 0:
        if len(usable_buttons) > 1:
            least_nonzero = usable_buttons[1]
        else:
            least_nonzero = -1
    else:
        least_nonzero = least_button

    print(get_closest_number())
