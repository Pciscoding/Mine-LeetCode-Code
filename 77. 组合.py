class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]  #存放符合条件结果的集合
        path=[]  #用来存放符合条件结果
        def backtrack(n,k):
            nonlocal path
            if k == 1:
                for i in range(1, n + 1):
                    path.append(i)
                    res.append(path.copy())
                    path.pop()
                return
            temp = path.copy()
            path.append(n)
            backtrack(n - 1, k - 1)
            if n > k:
                path = temp
                backtrack(n - 1, k)
        backtrack(n, k)
        return res
