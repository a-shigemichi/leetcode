class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        """
        Separates each integer in the input array into its individual digits.
        
        Args:
            nums: A list of positive integers
            
        Returns:
            A list containing all digits of the integers in nums in the same order
        """
        answer = []
        for num in nums:
            # Convert the number to a string and iterate through each digit
            for digit in str(num):
                answer.append(int(digit))
        return answer
