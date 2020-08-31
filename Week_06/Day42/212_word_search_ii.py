'''
leetcode: 212

给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
END_OF_WORD = "#"

class Solution:

    def findWords(self, board, words) :
        if not board or not board[0]: return []
        if not words: return []
        self.result = set()

        # 构建 Trie
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[END_OF_WORD] = END_OF_WORD

        self.m, self.n = len(board), len(board[0])
        for i in xrange(self.m):
            for j in xrange(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)
        return list(self.result)

        def _dfs(self, board, i, j, cur_word, cur_dict):
            cur_word += board[i][j]
            cur_dict = cur_dict[board[i][j]]
            if END_OF_WORD in cur_dict:
                self.result.add(cur_word)
            tmp, board[i][j] = board[i][j], '@'
            for k in xrange(4):
                x, y = i + dx[k], j + dy[k]
                if 0 <= x < self.m and 0 <= y < self.n \
                        and board[x][y] != '@' and board[x][y] in cur_dict:
                            self._dfs(board, x, y, cur_word, cur_dict)
            board[i][j] = tmp



# 1. words  遍历  -->  board search
# O(N*m*m*4^k)
#
# 2. trie
# a. all words  -->  trie  构建起 prefix
# b. board, DFS
# O(?)
