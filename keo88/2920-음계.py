import sys

lst = list(map(int, sys.stdin.readline().split()))

isAs, isDe = True, True

for i in range(len(lst)):
    if isAs and lst[i] != i + 1:
        isAs = False
    if isDe and lst[i] != len(lst) - i:
        isDe = False

if isAs:
    print('ascending')
elif isDe:
    print('descending')
else:
    print('mixed')

