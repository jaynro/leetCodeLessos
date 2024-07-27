def find_length(nums, k):
    # curr is the current sum of the window
    left = curr = ans = 0

    # 1.Expand the window to the right
    for right in range(len(nums)):
        curr += nums[right]

    # 2.Shrink the window from the left
        while curr > k:
            curr -= nums[left]
            left += 1
    # 3.Update the result
        ans = max(ans, right - left + 1)
    
    return ans

k=8
nums = [3,1,2,7,4,2,1,1,5]
print(find_length(nums, k)) # 4