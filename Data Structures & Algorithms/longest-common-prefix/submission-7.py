class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # T: O(n * m)
        # S: O(1)
        if not strs:
            return ""

        # Base on first string
        first = strs[0]

        for i in range(len(first)):
            char = first[i]

            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return s[:i]
        return first
        