class Solution:
    def twoSum(self, nums, target):
        # Create an empty hashmap (dictionary) to store value:index
        hashmap = {}

        # Loop through the list with both index (i) and value (num)
        for i, num in enumerate(nums):

            # Calculate the number needed to reach the target
            difference = target - num

            # Check if the needed number already exists in hashmap
            if difference in hashmap:
                # If yes, return the pair of stored index and current index
                return [hashmap[difference], i]
            else:
                # Otherwise, store the current num and its index in hashmap
                hashmap[num] = i

        # If no pair found
        return []


# ---- Test the function ----
solution = Solution()
nums = [2, 7, 11, 15]
target = 9

print(solution.twoSum(nums, target))
