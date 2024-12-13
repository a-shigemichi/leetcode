class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        for arr1_element in arr1:
            valid = True
            for arr2_element in arr2:
                if abs(arr1_element - arr2_element) <= d:
                    valid = False
                    break
            
            if valid:
                count += 1
        
        return count

def main():
    arr1 = [4,5,8]
    arr2 = [10,9,1,8]
    d = 2
    my_object = Solution()        
    res = my_object.findTheDistanceValue(arr1,arr2, d)
    print(res)

if __name__ == "__main__":
   main()