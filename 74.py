class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False



def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    my_object = Solution()        
    judgement = my_object.searchMatrix(matrix,target)
    print(judgement)

if __name__ == "__main__":
   main()