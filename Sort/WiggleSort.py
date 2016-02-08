class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        length = len(nums)//2
        end = nums[length]
        for i in range(1, len(nums), 2):
            if nums[-1] == end:
                break
            else:
                nums.insert(i, nums.pop())
        
        return nums

so = Solution()
print(so.wiggleSort([3, 5, 2, 1, 6, 4]))