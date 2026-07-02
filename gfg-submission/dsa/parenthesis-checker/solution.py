class Solution:
    def isBalanced(self, s):
        # code here
        hash_ = {'}': '{', ']': '[', ')': '('}
        
        stack = deque()
        
        def isempty(stack):
            return len(stack) == 0
            
        for brac in s:
            if brac in ['(', '[', '{']:
                stack.append(brac)
            else:
                if isempty(stack):
                    return False
                    
                ele = stack.pop()
                if hash_[brac] != ele: 
                    return False
        return isempty(stack)
