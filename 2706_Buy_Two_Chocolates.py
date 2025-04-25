class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        """
        Calculate the amount of money leftover after buying exactly two chocolates.
        
        Args:
            prices: An integer array representing the prices of various chocolates.
            money: An integer representing the initial amount of money.
            
        Returns:
            The amount of money leftover after buying two chocolates.
            If it's not possible to buy two chocolates without ending up in debt,
            return the initial amount of money.
            
        Example:
            Input: prices = [1,2,2], money = 3
            Output: 0
            Explanation: Buy the chocolates with prices [1,2]. You will have 3 - 1 - 2 = 0 money leftover.
            
            Input: prices = [3,2,3], money = 3
            Output: 3
            Explanation: You cannot buy 2 chocolates without ending up in debt, so return 3.
        """
        min1 = 101
        min2 = 101
        
        for price in prices:
            if price < min1:
                min2 = min1
                min1 = price
            elif price < min2:
                min2 = price
        
        total_cost = min1 + min2
        
        if total_cost <= money:
            return money - total_cost
        else:
            return money
        