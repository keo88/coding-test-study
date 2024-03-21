import sys
N = int(input())

def convertIp(ip):
    val = 0
    parts = ip.split('.')
    for part in parts:
        val <<= 8
        val += int(part)
    return val

def convertToIp(num):
    parts = [0] * 4
    
    for i in range(3, -1, -1):
        parts[i] = num % 256
        num >>= 8
    return '.'.join(map(str, parts))

ipNums = [convertIp(sys.stdin.readline()) for _ in range(N)]

commonIpNum = ipNums[0]
cnt = 0

def isSame(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            return False
    return True

while not isSame(ipNums):
    for j in range(N):
        ipNums[j] >>= 1
    cnt += 1

mask = 0xFFFFFFFF
mask >>= cnt
mask <<= cnt

print(convertToIp(mask & commonIpNum))
print(convertToIp(mask))
