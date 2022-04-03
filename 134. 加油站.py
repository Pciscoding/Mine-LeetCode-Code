#自己写的，用了后缀和的思想，虽然复杂度为O(n)，但是遍历次数达3次，不够理想
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus = []
        for i in range(len(gas)):
            surplus.append(gas[i] - cost[i])    #用一个列表来记录每个油站的盈余油量
        if sum(surplus) < 0:
            return -1
        else:
            for i in range(-2, -len(surplus) - 1, -1):
                surplus[i] += surplus[i + 1]    #后缀和，找后面可以加最多油的出发点
        return surplus.index(max(surplus))
            
#卡哥代码，遍历一次，优秀
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        curSum = 0
        totalSum = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if totalSum < 0: return -1
        return start
