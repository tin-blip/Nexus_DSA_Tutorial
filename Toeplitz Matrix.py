class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rownum = len(matrix) - 1
        colnum = len(matrix[0]) - 1
        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
