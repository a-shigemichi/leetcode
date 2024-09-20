class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res =[]
        count_1={}
        count_2={}
        for element in nums1:
            if element in count_1:
                count_1[element] += 1
            else:
                count_1[element] = 1
        for element in nums2:
            if element in count_2:
                count_2[element] += 1
            else:
                count_2[element] = 1
            if element in count_1 and count_2[element] <= count_1[element]:
                    res.append(element)
        return res




def main():
    nums1 = [1,2,2,1]
    nums2 = [2]
    my_object = Solution()        
    judgement = my_object.intersect(nums1,nums2)
    print(judgement)

if __name__ == "__main__":
   main()