def getDir(n):
    if n == 1:
        return (-1, 0)
    elif n == 2:
        return (-1, -1)
    elif n == 3:
        return (0, -1)
    elif n == 4:
        return (1, -1)
    elif n == 5:
        return (1, 0)
    elif n == 6:
        return (1, 1)
    elif n == 7:
        return (0, 1)
    else:
        return (-1, 1)

def deepCopy(b):
    nb = []
    for i in range(len(b)):
        nb.append(b[i].copy())
    return nb

b = []
curPos = {}
for i in range(4):
    arr = list(map(int, input().split()))
    output = []
    for j in range(4):
        output.append((arr[2 * j], arr[2 * j + 1]))
        curPos[arr[2 * j]] = (i, j)
    b.append(output)

spos = (0, 0)
sdir = b[0][0][1]
score = b[0][0][0]
ans = score
curPos[b[0][0][0]] = (-1, -1)
b[0][0] = (0, sdir)


def dfs(b, sharkPos, sdir, score, c):
    global ans
    sPoses = []
    sdirpos = getDir(sdir)
    for i in range(1, 4):
        n_x = sharkPos[0] + sdirpos[0] * i
        n_y = sharkPos[1] + sdirpos[1] * i
        if n_x < 0 or n_x >= 4 or n_y < 0 or n_y >= 4:
            break
        sPoses.append((n_x, n_y))
    if len(sPoses) == 0:
        ans = max(ans, score)
    
    for fish in range(1, 17):

        if c[fish] == (-1, -1):
            continue
        fishPos = c[fish]
        _, fdir = b[fishPos[0]][fishPos[1]]

        for adder in range(8):
            av = (fdir + adder) % 8
            fdirpos = getDir(av)
            n_x = fishPos[0] + fdirpos[0]
            n_y = fishPos[1] + fdirpos[1]
            if n_x < 0 or n_x >= 4 or n_y < 0 or n_y >= 4:
                continue
            if (n_x, n_y) == sharkPos:
                continue
            targetFish, targetDir = b[n_x][n_y] 
            if targetFish == 0:
                b[n_x][n_y] = (fish, av)
                c[fish] = (n_x, n_y)
                b[fishPos[0]][fishPos[1]] = (0, 0)
                break
            else:
                b[n_x][n_y] = (fish, av)
                b[fishPos[0]][fishPos[1]] = (targetFish, targetDir)
                c[fish] = (n_x, n_y)
                c[targetFish] = fishPos
                break


    for nsPos in sPoses:
        targetFish, targetDir = b[nsPos[0]][nsPos[1]]
        if targetFish == 0:
            ans = max(ans, score)
            continue
        nb = deepCopy(b)
        nc = c.copy()
        nb[nsPos[0]][nsPos[1]] = (0, sdir)
        nc[targetFish] = (-1, -1)
        nsDir = targetDir
        dfs(nb, nsPos, nsDir, score + targetFish, nc)


dfs(b, spos, sdir, score, curPos)
print(ans)
