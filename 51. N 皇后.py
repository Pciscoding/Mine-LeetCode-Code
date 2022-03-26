#自己做出来的答案，速度很快，棒棒
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = []
        occupy_row, occupy_diagonal_1, occupy_diagonal_2 = set(), set(), set()  #分别记录被占用的列，和方向正交的两种斜线

        def backtracking(j):    #逐行递归回溯，j代表的是行数
            if len(path) == n:
                res.append(path.copy())
                return

            for i in range(0, n):
                # (i + j)相等在同一条对角线上，同理(i - j)相等也在同一条对角线上
                if i not in occupy_row and i + j not in occupy_diagonal_1 and i - j not in occupy_diagonal_2:   #行肯定不会重复，要列和所在的两条斜线都没被占用才可进行递归
                    #print((i, j))
                    occupy_row.add(i)
                    occupy_diagonal_1.add(i + j)
                    occupy_diagonal_2.add(i - j)
                    str_temp = '.' * i + 'Q' + '.' * (n - i - 1)
                    path.append(str_temp)
                    backtracking(j + 1)
                    path.pop()
                    occupy_row.remove(i)
                    occupy_diagonal_1.remove(i + j)
                    occupy_diagonal_2.remove(i - j)
        
        backtracking(0)
        return res
