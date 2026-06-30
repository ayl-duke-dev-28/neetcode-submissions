class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        # Same trie root as before — nothing new here
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Identical to Trie insert — no changes needed
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        # Kick off the recursive helper from the root at index 0
        return self._search(self.root, 0, word)

    def _search(self, node: TrieNode, index: int, word: str) -> bool:
        # ── BASE CASE ──────────────────────────────────────────────
        # We've consumed every character in `word`
        # The answer depends on whether this node marks a complete word
        if index == len(word):
            return node.is_end

        ch = word[index]

        # ── CASE 1: Normal character ───────────────────────────────
        # Only one possible path forward
        if ch != '.':
            if ch not in node.children:
                return False                          # Dead end
            return self._search(node.children[ch], index + 1, word)

        # ── CASE 2: Wildcard '.' ───────────────────────────────────
        # Fan out: try every child this node has
        # This is the backtracking core — explore all, accept if any works
        for child_node in node.children.values():
            if self._search(child_node, index + 1, word):
                return True                           # Short-circuit: found a match

        return False                                  # No branch succeeded