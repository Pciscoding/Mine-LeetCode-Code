#自己写的代码，没有剪纸，额外维护一个字典来去重，超时了
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        #used_tciket = []
        path = []
        unused_index = set(range(0, len(tickets)))
        #print(temp_tickets)

        def backtracking():
            if len(path) == len(tickets) + 1:
                res.append(path.copy())
                return
            if len(path) == 0:
                for i in range(0, len(tickets)):
                    #print(t)
                    if i not in unused_index: continue
                    if tickets[i][0] == 'JFK':
                        unused_index.remove(i)
                        path.append(tickets[i][0])
                        path.append(tickets[i][1])
                        print(path)
                        backtracking()
                        path.pop()
                        path.pop()
                        unused_index.add(i)
            else:
                #print(temp_tickets)
                for i in range(0, len(tickets)):
                    if i not in unused_index: continue
                    if tickets[i][0] == path[-1]:
                        unused_index.remove(i)
                        path.append(tickets[i][1])
                        #print(path)
                        backtracking()
                        path.pop()
                        unused_index.add(i)
        backtracking()
        res.sort()
        return res
 

#答案法：
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # defaultdic(list) 是为了方便直接append
        tickets_dict = defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])
        '''
        tickets_dict里面的内容是这样的
         {'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        '''
        path = ["JFK"]
        def backtracking(start_point):
            # 终止条件
            if len(path) == len(tickets) + 1:
                return True
            # 排序，所以后面先找到的答案就是最优答案
            tickets_dict[start_point].sort()
            for _ in tickets_dict[start_point]:
                #必须及时删除，避免出现死循环
                end_point = tickets_dict[start_point].pop(0)
                path.append(end_point)
                # 只要找到一个就可以返回了，这里剪枝了，节省大量时间
                if backtracking(end_point):
                    return True
                path.pop()
                tickets_dict[start_point].append(end_point)

        backtracking("JFK")
        return path
