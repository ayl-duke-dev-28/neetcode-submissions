class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None          # Stores full word string at terminal node
                                  # (cleaner than is_end for this problem)

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        # ── STEP 1: Build trie from all words ─────────────────────
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word                  # Store the word at its terminal node

        results = []
        rows, cols = len(board), len(board[0])

        # ── STEP 2: DFS from every cell ───────────────────────────
        def dfs(r, c, trie_node):

            # ── PRUNING CONDITIONS ─────────────────────────────────
            if r < 0 or r >= rows:            # Out of bounds
                return
            if c < 0 or c >= cols:
                return
            if board[r][c] == '#':            # Already visited this cell
                return

            ch = board[r][c]
            if ch not in trie_node.children:  # This char not in trie = dead end
                return

            # ── ADVANCE TRIE ───────────────────────────────────────
            next_node = trie_node.children[ch]

            # ── WORD FOUND ─────────────────────────────────────────
            if next_node.word:
                results.append(next_node.word)
                next_node.word = None         # Deduplicate: clear so we don't
                                              # add the same word twice via
                                              # a different path on the board

            # ── CHOOSE: mark cell as visited ──────────────────────
            board[r][c] = '#'

            # ── EXPLORE: all 4 neighbors ───────────────────────────
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            # ── UN-CHOOSE: restore cell ────────────────────────────
            board[r][c] = ch

        # Launch DFS from every cell on the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return results