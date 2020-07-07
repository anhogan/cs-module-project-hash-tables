class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index_mapping = {}

    # Go through the set of nums
    # Access to current num
    # Look for target - num
    # If complement is in dict
      # return the indices
    # If not, add num to dict

    # Keep track of indexes, not nums themselves
    for i in range(len(nums)):
      current_num = nums[i]
      complement = target - current_num

      if complement in index_mapping:
        # Return the index for complement and the current index
        return [index_mapping[complement], i]
      else:
        index_mapping[current_num] = i