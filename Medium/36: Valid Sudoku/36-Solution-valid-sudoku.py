class Solution(object):
    # function checking if any number repeats
    def repNumber(self, numList):
        repDict = {}
        for x in numList:
            if x.isalnum() and x != '.':
                if x in repDict:
                    return False
                repDict[x] = True
        return True    

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check rows for duplicates
        for x in board:
            if not self.repNumber(x):
                return False
        
        # Check columns for duplicates
        for i in range(9):
            colList = []
            for j in range(9):
                colList.append(board[j][i])
            if not self.repNumber(colList):
                return False
        
        # Check 3x3 squares for duplicates
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square = []
                for i in range(3):
                    for j in range(3):
                        square.append(board[row + i][col + j])
                if not self.repNumber(square):
                    return False

        return True
