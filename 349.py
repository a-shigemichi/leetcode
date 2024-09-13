class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        


def main():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    my_object = Solution()        
    judgement = my_object.intersection(nums1,nums2)
    print(judgement)

if __name__ == "__main__":
   main()