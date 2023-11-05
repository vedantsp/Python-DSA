"""
        Set Matrix Zeroes

        """


class Solution:

    def setZeroes(self, matrix: List[List[int]]):

        row = set()
        column = set()
        
    
     for i in range(len(matrix[0])):
         for j in range(len(matrix)):
             if matrix[i][j] == 0:
                 row.add(i)
                 column.add(j)

     for i in row:
        for j in range(len(matrix[0])):
            martix[i][j] = 0


     for i in column:
         for j in range(len(matrix())):
             matrix[j][i] = 0               

