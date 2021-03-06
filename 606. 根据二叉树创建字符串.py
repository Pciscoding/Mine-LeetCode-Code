官解注释：
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        if root.left is None and root.right is None:#无左无右，直接加中，左不用空括号
            return str(root.val)
        if root.right is None:#无右，加中和（左）
            return f"{root.val}({self.tree2str(root.left)})"
        return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"#剩下的情况：有左有又或无左有又，都得加括号

自己代码：
class Solution:
    res = ''
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return None
        self.res += str(root.val)
        if root.left:
            self.res += '('
            self.tree2str(root.left)
            self.res += ')'
        elif root.right:
            self.res += '()'
        if root.right: 
            self.res += '('
            self.tree2str(root.right)
            self.res += ')'
        return self.res

非迭代法，难度直增，而且不算快：
class Solution:
    res = ''
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return None
        stack = [root]
        res = ''
        be_added = set()
        while stack:
            node = stack.pop()
            if node in be_added:
                res += ')'
            else:
                res += '('
                res += str(node.val)                
                stack.append(node)                        
                if node.right:                        
                    stack.append(node.right)
                if node.left:                    
                    stack.append(node.left)
                elif node.right:
                    res += '()'
                be_added.add(node)
        return res[1: len(res) - 1]
