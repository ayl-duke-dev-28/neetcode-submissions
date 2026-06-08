class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = set()
        b = []
        final = []
        str_length = len(strs)

        for i in range(str_length):
            sorted_anagram = sorted(strs[i])
            a.add("".join(sorted_anagram))

        for key in a:
            for j in range(str_length):
                if "".join(sorted(strs[j])) == key:
                    b.append(strs[j])
            final.append(b)
            b = []

        return final
            