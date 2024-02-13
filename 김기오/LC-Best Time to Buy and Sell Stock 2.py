class Solution(object):
    def maxProfit(self, prices):
        prof = 0
        isHold = False
        lastLeast = prices[0]
        lastBest = -1
        for p in prices:
            # print(f'p {p} lastBest {lastBest} lastLeast: {lastLeast}')
            if isHold:
                if lastBest > p:
                    # sell
                    prof += lastBest - lastLeast
                    isHold = False
                    lastBest = -1
                    lastLeast = p
                else:
                    lastBest = p
            else:
                if lastLeast < p:
                    # buy
                    isHold = True
                    lastBest = p
                else:
                    lastLeast = p
            
        if lastBest  > lastLeast and isHold:
            prof += lastBest - lastLeast
        return prof
