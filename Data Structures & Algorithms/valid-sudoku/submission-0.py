class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        col = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        sq = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}

        for i in range(0,9):
            for j in range(0,9):

                if board[i][j] == ".":
                    continue

                if (board[i][j] in row[i] or
                    board[i][j] in col[j] or
                    board[i][j] in sq[i//3 * 3 + j//3]):
                    return False

                row[i].append(board[i][j])
                col[j].append(board[i][j])
                sq[i//3 * 3 + j//3].append(board[i][j])

        return True