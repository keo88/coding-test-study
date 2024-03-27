import sys

N = int(input())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = {}

for i in range(N - 1, -1, -1):
    days, price = arr[i]
    if i + days > N:

        if i + 1 in dp:
            dp[i] = dp[i + 1]
        else:
            dp[i] = 0
        continue
    if not i + days in dp:
        dp[i+days] = 0
    dp[i] = max(dp[i + days] + price, dp[i + 1] if i + 1 in dp else 0)

print(dp[0])

