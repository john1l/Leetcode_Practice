from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
       
         rows , cols  = defaultdict(set) , defaultdict(set)
         triples ,visit = defaultdict(set), deque([])

         for r in range(9):
             for c in range(9):
                 if board[r][c] != '.':
                     rows[r].add(board[r][c])
                     cols[c].add(board[r][c])
                     triples[(r//3,c//3)].add(board[r][c])
                 else: 
                     visit.append((r,c))

         def dfs():
             if not visit:
                 return True 
             r,c = visit[0]
             t = (r//3, c //3 )
             for dig in { str(e) for e in range(1,10) }:
                 if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
                     board[r][c] = dig 
                     rows[r].add(dig)
                     cols[c].add(dig)
                     triples[t].add(dig)
                     visit.popleft()
                     if dfs():
                         return True 
                     else:
                         board[r][c] = '.'
                         rows[r].discard(dig)
                         cols[c].discard(dig)
                         triples[t].discard(dig)
                         visit.appendleft((r,c))
             return False 
         dfs()

