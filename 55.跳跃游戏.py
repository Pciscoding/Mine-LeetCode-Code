#自己写法，时间复杂度O(n^2)，太慢了！但是用来做45题很快
class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        cur = 0
        while nums[cur] != 0 and cur < len(nums) - 1:
            if cur + nums[cur] >= len(nums) - 1:
                return True
            max_jump = 0
            for i in range(cur + 1, nums[cur] + cur + 1):   #i 表示当前能跳到的范围
                if i + nums[i] > max_jump:
                    max_jump = i + nums[i]
                    cur = i
        
        return False
#看官解后更改，把每一步能跳的距离看作能量
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        energy = nums[0]
        i = 0
        while energy != 0:
            i += 1
            energy -= 1
            if energy < nums[i]:
                energy = nums[i]
            if i + energy >= len(nums) - 1:
                return True
        return False
