class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(n,n,'',ans)
        return ans
        
    def dfs(self,left,right,path,ans):
        if left>right or left<0 or right<0:
            return
        
        if left == 0 and right == 0:
            ans.append(path)
            
        self.dfs(left-1,right,path+'(',ans)
        self.dfs(left,right-1,path+')',ans)
        
        
        