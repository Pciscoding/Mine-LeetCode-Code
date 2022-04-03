#自己写的
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        res, cur = 0, 0
        while nums[cur] != 0 and cur < len(nums) - 1:
            if cur + nums[cur] >= len(nums) - 1:    #
                return res + 1
            max_jump = 0
            temp = cur
            for i in range(cur + 1, nums[cur] + cur + 1):   #i 表示当前能跳到的范围
                if i + nums[i] > max_jump:
                    max_jump = i + nums[i]
                    cur = i
            if temp != cur:
                res += 1
        return res
        
#官解，更加简洁，思路一样
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
