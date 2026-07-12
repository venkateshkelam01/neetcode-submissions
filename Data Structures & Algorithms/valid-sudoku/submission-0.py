class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                value = board[r][c]

                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in squares[(r // 3, c // 3)]
                ):

                  return False

                cols[c].add(value)
                rows[r].add(value)
                squares[(r//3, c//3)].add(value)
        return True


