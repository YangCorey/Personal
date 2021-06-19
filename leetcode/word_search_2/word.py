from typing import List
class Solution:
    def dfs(self, trie, r, c, res):
        if "#" in trie and res not in self.found:
            self.found.append(res)

        if r < 0 or r >= len(self.board) or c < 0 or c >= len(self.board[0]):
            return
        if self.board[r][c] in trie and self.board[r][c] != "#":
            temp_board = self.board[r][c]
            self.board[r][c] = "#"
            self.dfs(trie[temp_board], r - 1, c, res + temp_board)
            self.dfs(trie[temp_board], r + 1, c, res + temp_board)
            self.dfs(trie[temp_board], r, c - 1, res + temp_board)
            self.dfs(trie[temp_board], r, c + 1, res + temp_board)
            self.board[r][c] = temp_board


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            temp_trie = trie
            for char in word:
                if char not in temp_trie:
                    temp_trie[char] = {}
                temp_trie = temp_trie[char]
            temp_trie["#"] = "#"
        self.found = []
        self.board = board
        for r in range(len(board)):
            for c in range(len(board[r])):
                self.dfs(trie, r, c, "")
        #Make the trie with the word list
        #Iterating through each space in board run dfs
        #Check if this letter is in the trie if so 
        return list(self.found)
sol = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain", "odd"]

board = [["o","a","a","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]
#board = [["a","b"],["c","d"]]
#words = ["abcb"]
print(sol.findWords(board = board, words = words))
