'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Inititalize the result list:
        merged = []

        # Iterate through both strings simutaneously:
        for i in range(min(len(word1), len(word2))):
            merged.append(word1[1]) # Add character from word1
            merged.append(word2[1]) # Add character from word2
        
        # Add any remaining characters from the longer string
        merged.append(word1[i+1:])
        merged.append(word2[i+1:])

        # Join the list into a single string and return it
        return ''.join(merged)