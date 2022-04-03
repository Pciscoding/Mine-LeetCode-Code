#自己写的代码，冗长的逻辑判断...
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        #print(nums)
        i = 0
        while k > 0:
            if i < len(nums):
                if nums[i] < 0:
                    nums[i] = -nums[i]
                elif nums[i] == 0:
                    break
                else:
                    if k % 2 == 0:
                        break
                    elif i > 0 and nums[i - 1] < nums[i]:
                        nums[i - 1] = - nums[i - 1]
                        break
                    else:
                        nums[i] = -nums[i]
                        break
            elif k % 2 == 0:
                break
            else:
                nums[-1] = -nums[-1]
                break
            i += 1
            k -= 1
        return sum(nums)
      
#卡哥写法，简介！
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A = sorted(A, key=abs, reverse=True) # 将A按绝对值从大到小排列
        for i in range(len(A)):
            if K > 0 and A[i] < 0:
                A[i] *= -1
                K -= 1
        if K > 0:
            A[-1] *= (-1)**K #取A最后一个数只需要写-1
        return sum(A)
