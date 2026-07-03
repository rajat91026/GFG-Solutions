class Solution:
    def sumOfMatrix(self, mat: list[list[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                sum +=mat[i][j]
        return sum
            
        
        # code here
        