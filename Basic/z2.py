class Solution:
    def largestElement(self, nums):

        largest = nums[0]

        for num in nums:
            if num < largest:
                largest = num

        return largest


nums = [2, 5, 3, 6, 7]

obj = Solution()
result = obj.largestElement(nums)

print(result)