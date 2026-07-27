class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_sets = [set()]*9
        row_sets = [set()]*9
        quarter_sets = [set()]*9
        for row_num in range(len(board)):
            for column_num in range(row_num):
                element = board[row_num][column_num]
                if element in column_sets[column_num]:
                    return False
                if element in row_sets[row_num]:
                    return False
                quarter_num = int(((row_num//3) * 3) + (column_num//3))
                print(row_num, row_num//3, column_num, column_num//3, quarter_num)
                if element in quarter_sets[quarter_num]:
                    return False
                column_sets[column_num].add(element)
                row_sets[row_num].add(element)
                quarter_sets[quarter_num].add(element)
        return True
                
