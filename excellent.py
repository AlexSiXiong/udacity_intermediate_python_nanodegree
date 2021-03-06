"""This is the extension module.

Implement a trie node improving the search efficiency.
"""


class TrieNode:
    """Trie node is the basic element of a trie tree."""

    def __init__(self):
        """Init child_node dictionary."""
        self.child_node = {}
        self.isEnd = None


class Trie:
    """Trie is used in get_neo_name in database.py."""

    def __init__(self, mapping_dict):
        """Create the root trie node and build the tree once it is initiated."""
        self.tree = TrieNode()
        self._make_trie_tree(mapping_dict)

    def _make_trie_tree(self, mapping_dict):
        """Create a trie tree."""
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
        """Search function."""
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