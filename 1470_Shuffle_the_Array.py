class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffle_nums=[]

        for idx in range(n):
            shuffle_nums.append(nums[idx])
            shuffle_nums.append(nums[idx+n])

        return  shuffle_nums
            