class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        st = [] 
        res = [] 
        #openN = closeN = 0 
        def backtrack(openN, closeN):


            if openN == closeN == n:
                res.append( ''.join(st) ) 
                return   
            if openN < n: 
                st.append('(')
                backtrack(openN+1 ,closeN)
                st.pop()
            if closeN < openN:
                st.append(')')
                backtrack(openN , closeN+1) 
                st.pop()

        backtrack(0,0) 
        return res 


