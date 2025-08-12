def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    nums.sort()
    while left < right:
        s = nums[left] + nums[right]
        
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

