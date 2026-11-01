class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding Window
        # Hash Map
        # T: O(m + n)
        # S: O(m + n)
        if (
            not s or not t or
            len(s) < len(t)
        ):
            return ""

        target = {}
        for c in t:
            target[c] = target.get(c, 0) + 1

        need, have = len(target), 0
        res_range, min_length = (-1, -1), float('inf')

        window = {}
        L = 0
        for R in range(len(s)):
            c = s[R]
            window[c] = window.get(c, 0) + 1

            if c in target and window[c] == target[c]:
                have += 1
            
            while have == need:
                length = R - L + 1
                if length < min_length:
                    min_length = length
                    res_range = (L, R + 1)

                window[s[L]] -= 1
                if s[L] in target and window[s[L]] < target[s[L]]:
                    have -= 1
                L += 1
        
        L_res, R_res = res_range
        return s[L_res : R_res] if min_length != float('inf') else ""
