#就是把所有能钱的机会都赚了，那什么是能赚钱的机会呢，就是股票上涨的时候，所以只要把所有上涨的区间能赚的钱加起来就好
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                res += prices[i] - prices[i - 1]
        return res
