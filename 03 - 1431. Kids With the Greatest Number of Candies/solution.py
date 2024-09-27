'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        return [candy + extraCandies >= mx for candy in candies]
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Step 1: Find the maximum number of candies any kid currently has:
        max_candies = max(candies)

        # Step 2: Create a result list where each element is True or False:
        result = []
        for candy in candies:
            # Check if the current kid's candies + extraCandies is at leat the max
            result.append(candy + extraCandies >= max_candies)

        return result
