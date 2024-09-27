'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        i, j = 0, len(s) - 1
        cs = list(s)
        while i < j:
            while i < j and cs[i] not in vowels:
                i += 1
            while i < j and cs[j] not in vowels:
                j -= 1
            if i < j:
                cs[i], cs[j] = cs[j], cs[i]
                i, j = i + 1, j -1
        return "".join(cs)
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define vowels:
        vowels = set('aeiouAEIOU')

        # Convert string to list because strings are immutable in Python(and most languages):
        s = list(s)

        # Initialize two pointers:
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer until it finds a vowel:
            if s[left] not in vowels:
                left += 1
                continue

            # Move right pointer until it finds a vowel:
            if s[right] not in vowels:
                right -= 1
                continue

            # Swap the vowels:
            s[left], s[right] = s[right], s[left]

            # Move both pointers:
            left += 1
            right -= 1

        # Convert list back to string and return:
        return ''.join(s)