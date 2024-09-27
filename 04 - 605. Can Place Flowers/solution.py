'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i  in range(1, len(flowerbed) - 1):
            # Plant a flower
            if sum(flowerbed[i - 1 : i + 2]) == 0:
                flowerbed[i] = 1
                n -= 1

                # If all flowers are planted, return True
                if n == 0:
                    return True

        # If not all flowers are planted, return False
        return n <= 0
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Step 1: Handle edge case where no flowers need to be planted:
        if m == 0:
            return True

        # Step 2: Travesse the flowerbed  to plant flowers:
        for i in range(len(flowerbed)):
            # Check the previous and next plot is empty and its adjacent plots are also empty:
            if flowerbed[i] == 0:
                # Check the previous and next plot (handle edge cases at boundaries):
                empty_prev (i == 0 or flowerbed[i - 1] == 0) # Either it's the first plot or the one before is empty;
                empty_next (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0) # Either it's the last plot or the next one is empty;

                if empty_prev and empty_next:
                    # Plant a flower in the current plot:
                    flowerbed[i] = 1
                    n -= 1 # Decrement n as we planted one flower;

                    # If we've planted all required flowers, return True:
                    if n == 0:
                        return True

        # if we finish checking and haven't planted all flowers, return False:
        return False
