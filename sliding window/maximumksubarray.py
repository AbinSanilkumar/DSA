class Solution:
    def maxSumSubarray(self, nums, k):

        window_sum = sum(nums[:k])

        max_sum = window_sum

        for right in range(k, len(nums)):

            window_sum = window_sum - nums[right - k] + nums[right]

            max_sum = max(max_sum, window_sum)

        return max_sum