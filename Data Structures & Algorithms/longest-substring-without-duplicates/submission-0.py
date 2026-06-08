class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_len = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                chars.remove(s[left])
                left += 1

        return max_len