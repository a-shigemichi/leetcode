class Solution(object):
    def removeFreeCandies(self, cost, candy_points):
        if len(cost) > 0:
            cost.pop()
        candy_points = 0
        return cost, candy_points
    
    def minimumCost(self, cost):
        cost.sort()
        min_total_cost = 0
        candy_points = 0
        
        while len(cost) > 0:
            min_total_cost += cost.pop()
            candy_points += 1
            if candy_points == 2:  
                cost, candy_points = self.removeFreeCandies(cost, candy_points)
        
        return min_total_cost


def main():
    cost = [1, 2, 3]
    my_object = Solution()        
    res = my_object.minimumCost(cost)
    print(res)

if __name__ == "__main__":
    main()