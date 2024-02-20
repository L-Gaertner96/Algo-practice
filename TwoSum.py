class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store elements and their indices
        num_to_index = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate complement
            complement = target - num
            
            # Check if complement exists in dictionary
            if complement in num_to_index:
                # Return indices if found
                return [num_to_index[complement], i]
            
            # Store current element and its index in dictionary
            num_to_index[num] = i