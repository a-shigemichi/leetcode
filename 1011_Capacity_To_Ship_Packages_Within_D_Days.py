class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def can_ship_within_days(capacity):
            days_needed = 1
            current_load = 0
            
            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = weight
                else:
                    current_load += weight
                    
                if days_needed > days:
                    return False
                    
            return True

        left = max(weights)
        right = sum(weights)  
      
        while left < right:
            mid = (left + right) // 2
            if can_ship_within_days(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
        




def main():
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    my_object = Solution()        
    judgement = my_object.shipWithinDays(weights,days)
    print(judgement)

if __name__ == "__main__":
   main()