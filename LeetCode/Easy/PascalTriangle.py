class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j < 1 or j == i:
                    row.append(1)
                else:
                    node = pascal[i-1][j-1] + pascal[i-1][j]
                    row.append(node)
            pascal.append(row)
        return pascal