#自己写的，还行
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        #用一个参数desc来表示当前元素之前得升降状态，1表示下降，-1表示上升，0表示不变
        if len(nums) == 1:
            return 1
        #如果只有一个数，直接返回1；否则先考虑前两个数，给desc赋一个初值
        if nums[1] > nums[0]:
            desc = -1
            res = 2
        elif nums[1] < nums[0]:
            desc = 1
            res = 2
        else:
            res = 1
            desc = 0
        #循环迭代后面的数，若现在这个数较上一个数上升(下降)，且之前的趋势在下降(上升)(desc=1 (-1))则序列长度+1，并把desc复制为-1(1)；
        #若上一个数亦在上升，则继续循环；若当前数较上一个数不变，则不做任何操作，继续循环，此时desc将继续保存前面的变化趋势
        for i in range(2, len(nums)):
            #print(desc)
            if nums[i] > nums[i - 1]:
                if not desc == -1:
                    res += 1 
                desc = -1
            elif nums[i] < nums[i - 1]:
                if not desc == 1:
                    res += 1
                desc = 1    
        return res
            


            
#卡哥解答，简介优雅
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        preC,curC,res = 0,0,1  #题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度
        for i in range(len(nums) - 1):
            curC = nums[i + 1] - nums[i]
            if curC * preC <= 0 and curC !=0:  #差值为0时，不算摆动
                res += 1
                preC = curC  #如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
        return res
