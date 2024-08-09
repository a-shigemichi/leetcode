class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res






def main():
    # nums = [1,2,3,1]
    nums = [1,1,1,2,2,3]
    k = 2
    my_object = Solution()        
    judgement = my_object.topKFrequent(nums,k)
    print(judgement)

if __name__ == "__main__":
   main()