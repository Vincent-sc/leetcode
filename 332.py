class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [-1] * (amount+1)
        res[0] = 0
        for i in range(1,amount+1):
            res[i] = amount+1
            for j in coins:
                if j <= i and res[i-j] > -1:
                    res[i] = min(res[i],res[i-j] + 1)
            if res[i] == amount+1:
                res[i] = -1
        return res[amount]
