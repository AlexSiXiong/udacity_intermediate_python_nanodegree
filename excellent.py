class TrieNode:
    def __init__(self):
        self.child_node = {}
        self.isEnd = None


class Trie:
    def __init__(self, mapping_dict):
        self.tree = TrieNode()
        self._make_trie_tree(mapping_dict)

    def _make_trie_tree(self, mapping_dict):
        for name, searching_obj in mapping_dict.items():
            cur_node = self.tree
            if name is None:
                continue
            for ch in name:
                if ch not in cur_node.child_node:
                    cur_node.child_node[ch] = TrieNode()
                cur_node = cur_node.child_node[ch]
            # print(searching_obj) # debug
            cur_node.isEnd = searching_obj

    def search(self, name):
        cur_node = self.tree
        for ch in name:
            if ch not in cur_node.child_node:
                return None
            cur_node = cur_node.child_node[ch]
        return cur_node.isEnd


if __name__ == '__main__':
    test_dict = {
        'alex1': 'Tom',
        'alex2': 'Jack',
        'may': 'ban'
    }
    t = Trie(test_dict)
    print(t.search('alex2'))