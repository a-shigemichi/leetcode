class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        result = set()
        
        for num in nums2:
            if num in set1:
                result.add(num)
        
        return list(result)


def main():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    my_object = Solution()        
    judgement = my_object.intersection(nums1,nums2)
    print(judgement)

if __name__ == "__main__":
   main()