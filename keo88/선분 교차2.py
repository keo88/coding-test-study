import sys


def get_coverage(x1, x2, x3, x4):
    sx_l1, lx_l1 = min(x1, x2), max(x1, x2)
    sx_l2, lx_l2 = min(x3, x4), max(x3, x4)
    same_x_start = max(sx_l1, sx_l2)
    same_x_end = min(lx_l1, lx_l2)
    return same_x_start, same_x_end


def get_inner_cut_y(x1, x2, y1, y2, x):
    d_x1, d_x2 = abs(x1 - x), abs(x2 - x)
    if d_x1 + d_x2 != 0:
        y_l1 = (d_x2 * y1 + d_x1 * y2) / (d_x1 + d_x2)
        return y_l1
    else:
        return None


def check():
    same_x_start, same_x_end = get_coverage(x1, x2, x3, x4)
    if same_x_start > same_x_end:
        return False
    else:
        if x1 == x2:
            if x3 == x4:
                same_y_start, same_y_end = get_coverage(y1, y2, y3, y4)
                if same_y_start > same_y_end:
                    return False
                else:
                    return True
            else:
                l2_y = get_inner_cut_y(x3, x4, y3, y4, same_x_start)
                if y1 <= l2_y <= y2:
                    return True
                else:
                    return False
        elif x3 == x4:
            l1_y = get_inner_cut_y(x1, x2, y1, y2, same_x_start)
            if y3 <= l1_y <= y4:
                return True
            else:
                return False

        same_x_start_y_l1 = get_inner_cut_y(x1, x2, y1, y2, same_x_start)
        same_x_start_y_l2 = get_inner_cut_y(x3, x4, y3, y4, same_x_start)
        if same_x_start_y_l1 == same_x_start_y_l2:
            return True
        elif same_x_start_y_l1 > same_x_start_y_l2:
            res1 = 1
        else:
            res1 = -1
        same_x_end_y_l1 = get_inner_cut_y(x1, x2, y1, y2, same_x_end)
        same_x_end_y_l2 = get_inner_cut_y(x3, x4, y3, y4, same_x_end)
        if same_x_end_y_l1 == same_x_end_y_l2:
            return True
        elif same_x_end_y_l1 > same_x_end_y_l2:
            res2 = 1
        else:
            res2 = -1
        if res1 * res2 == 1:
            return False
        else:
            return True


x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
print(1 if check() else 0)
