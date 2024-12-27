class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        
        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        
        return False
    
def main():
    arr = [10,2,5,3]
    my_object = Solution()        
    res = my_object.checkIfExist(arr)
    print(res)

if __name__ == "__main__":
   main()