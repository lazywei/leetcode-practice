class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] < nums[i+2]:
                return True
        return False


s = Solution()
print(s.increasingTriplet([1, 2, 3, 4, 5]))
print(s.increasingTriplet([5, 4, 3, 2, 1]))
print(s.increasingTriplet([5, 2, 5, 4, 5]))
