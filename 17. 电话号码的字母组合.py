class Solution:
    morphism = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        path = ''
        digits = list(digits)
        digits.reverse()
        def backtracking():
            nonlocal digits, path
            if len(digits) == 0:
                res.append(path)
                return
            i = int(digits.pop())
            for s in self.morphism[i]:
                path += str(s)
                backtracking()
                path = path[: -1]
            digits.append(i)
        backtracking()
        return res
