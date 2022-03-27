class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #思路:排序 + 贪心
        #为了尽可能满足最多数量的孩子，从贪心的角度考虑，应该按照孩子的胃口从小到大的顺序依次满足每个孩 子，且对于每个孩子，应该选择可以满足这个孩子的胃口且尺寸最小的饼干
        g.sort()
        s.sort()
        res = 0
        g_index, s_index = 0, 0
        while s_index < len(s) and g_index < len(g):
            if g[g_index] <= s[s_index]:
                g_index += 1
                s_index += 1
                res += 1
            else:
                s_index += 1
        return res
