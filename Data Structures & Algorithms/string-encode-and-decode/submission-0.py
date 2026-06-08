from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded += str(len(strs[i])) + "#" + strs[i]
        return encoded


    def decode(self, s: str) -> List[str]:
        a = []
        i = 0

        for _ in range(len(s)):   # we control i manually
            if i >= len(s):
                break

            length_str = ""

            # read number until '#'
            for j in range(i, len(s)):
                if s[j] == "#":
                    break
                length_str += s[j]

            length = int(length_str)

            # move i to start of actual string
            i = j + 1

            # grab exactly length characters
            a.append(s[i:i+length])

            # move i forward to next block
            i += length

        return a