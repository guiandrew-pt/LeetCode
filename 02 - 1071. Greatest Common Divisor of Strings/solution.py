'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        n = gcd(len(str1), len(str2)) 
        return str1[:n]
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Find the GCD of the lengths of str1 and str2 
        gcd_length = math.gcd(len(str1), len(str2))

        # Step 2: Get the substring of the length gcd_length
        candidate = str1[:gcd_length]

        # Step 3: Check if the candidate can form both str1 and str2 by repetition
        if candidate * (len(str1) // gcd_length) == str1 and candidate * (len(str2) // gcd_length) == str2:
            return candidate
        else:
            return ""
