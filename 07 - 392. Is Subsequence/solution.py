class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer, t_pointer = 0, 0

        # Traverse through t with t_pointer
        while t_pointer < len(t) and s_pointer < len(s):
            if t[t_pointer] == s[s_pointer]:
                # Move the s_pointer when there's a match
                s_pointer += 1
            # Always move the t_pointer
            t_pointer += 1

        # If we've gone through all of s, it's a subsequence
        return s_pointer == len(s)