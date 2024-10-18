class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        res =[]
        i=0
        j=0
        if n==0:
          return nums1
        while nums1[i] != 0 and i < m+n and m!=0:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while j < n:
            res.append(nums2[j])
            j+=1
        return res


def main():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    my_object = Solution()        
    judgement = my_object.merge(nums1,m,nums2,n)
    print(judgement)

if __name__ == "__main__":
   main()