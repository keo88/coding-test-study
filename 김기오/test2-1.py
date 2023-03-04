def solution(image):
    images = list(image.strip())
    answer = []
    acc = 0
    inferred_type = 0 # 0: init 1: possible <> or >, -1: possible <> or <
    for i in range(len(images)):
        if images[i] == '-':
            acc += 1
        elif images[i] == '<':
            if acc > 0:
                if inferred_type == -1:
                    answer.append([-1, acc])
                    inferred_type = 0
                acc = 0
            inferred_type = -1
        elif images[i] == '>':
            if acc > 0:
                if inferred_type == 0:
                    answer.append([1, acc])
                elif inferred_type == -1:
                    answer.append([0, acc])
                acc = 0
                inferred_type = 0

    if acc > 0:
        if inferred_type == -1:
            answer.append([-1, acc])
        acc = 0

    return answer

print(solution('<--->'))