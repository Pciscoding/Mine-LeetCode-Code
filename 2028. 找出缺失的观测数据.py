#自己用回溯算法写的 230ms 太慢
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        rest_sum = ((len(rolls) + n) * mean - sum(rolls))
        res = []
        if rest_sum / n > 6 or rest_sum / n < 1:
            return []
        def backtracking(rest_sum, n):
            if n == 0 and sum(res) == rest_sum:
                return True
            
            for i in range(rest_sum // n, min(round(rest_sum / n) + 1, 7)):
                if rest_sum % n == 0:
                    res.extend([int(rest_sum / n)] * n)
                    return True
                else:
                    res.append(i)
                    if backtracking(rest_sum - i, n - 1): return True
                    n += 1
        if backtracking(rest_sum, n):
            return res
        else:
            return []
#官解使用数学技巧90ms，很快！思路是把可以求得剩余和missingSum，在这个值符合体条件的情况下，把他除以n，得q余r，在创建一个数组，包含n - r个q和r个q + 1，这便是所求答案        
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missingSum = mean * (n + len(rolls)) - sum(rolls)
        if not n <= missingSum <= n * 6:
            return []
        quotient, remainder = divmod(missingSum, n)
        return [quotient + 1] * remainder + [quotient] * (n - remainder)
