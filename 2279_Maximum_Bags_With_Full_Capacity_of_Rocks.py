class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        remaining_space = []
        for i in range(len(capacity)):
            remaining_space.append(capacity[i] - rocks[i])

        remaining_space.sort()
        full_bags = 0
        for space in remaining_space:
            if additionalRocks >= space:
                additionalRocks -= space
                full_bags += 1
            else:
                break
                
        return full_bags
        

def main():
    capacity = [2,3,4,5]
    rocks = [1,2,4,4]
    additionalRocks = 2
    my_object = Solution()        
    res = my_object.maximumBags(capacity,rocks,additionalRocks)
    print(res)

if __name__ == "__main__":
   main()