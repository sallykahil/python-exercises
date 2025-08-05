def three_sum(nums):
    nums.sort()  # Step 1: Sort the array
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicate elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Step 2: Fix the first number
        left = i + 1
        right = len(nums) - 1

        # Step 3: Use two pointers
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for second and third number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1  # move right to get a bigger number

            else:
                right -= 1  # move left to get a smaller number

    return result
print(three_sum([-1, 0, 1, 2, -1, -4]))
 