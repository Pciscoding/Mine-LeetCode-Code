class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        s = str(num)
        if int(s[0] + s[1]) < 26:
            win = [1] + [2] + [2]
        else:
            win = [1] * 3
        for i in range(2, len(s)):
            if s[i - 1] != '0' and int(s[i - 1] + s[i]) < 26:
                win[2] = win[0] + win[1]    
            else:
                win[2] = win[1]
            win[0] = win[1]
            win[1] = win[2]
            
        return win[2]
