class Solution:
    def trimMean(self, arr: List[int]) -> float:
      """
      Calculate the mean after removing smallest 5% and largest 5% of elements.
      
      Args:
          arr (List[int]): Array of integers
          
      Returns:
          float: Mean of remaining elements after trimming

      """
      n = len(arr)
      remove_count = n * 5 // 100
      
      arr.sort()

      total = sum(arr[remove_count:n-remove_count])

      return total / (n - 2 * remove_count)
