import unittest
import btree

class TestBTree(unittest.TestCase):
    
    def test_b_search(self):
        D = [3,6]

        self.assertEqual(btree.b_search(2,D), 0)
        self.assertEqual(btree.b_search(3,D), 0)
        self.assertEqual(btree.b_search(4,D), 1)
        self.assertEqual(btree.b_search(7,D), 2)

    def test_search_morethan_root(self):
        #   3 - - 
        #   /      \
        # 1 2 -    3 4 -

        tree = btree.Tree(3)

        tree.root = btree.Node()
        tree.root.keys = [3]

        left = btree.Node()
        left.keys = [1,2]

        right = btree.Node()
        right.keys = [3,4]

        tree.root.children = [left, right]

        insert_pos, leaf_node = tree.search(4)
        self.assertEqual(insert_pos, 1)
        self.assertEqual(leaf_node.keys[0], 3)
        self.assertEqual(leaf_node.keys[1], 4)

        insert_pos, leaf_node = tree.search(5)
        self.assertEqual(insert_pos, 2)
        self.assertEqual(leaf_node.keys[0], 3)
        self.assertEqual(leaf_node.keys[1], 4)

    def test_search_only_root(self):
        tree = btree.Tree(3)
        tree.root = btree.Node()
        tree.root.keys = [2,5,8]

        insert_pos, leaf_node = tree.search(5)
        self.assertEqual(insert_pos, 1)

        insert_pos, leaf_node = tree.search(6)
        self.assertEqual(insert_pos, 2)

    def test_insert_no_root(self):
        tree = btree.Tree(3)
        tree.insert(6, value=5)

        self.assertListEqual(tree.root.keys, [6])
        self.assertListEqual(tree.root.values, [5])

        tree.insert(5, value=3)
        
        self.assertListEqual(tree.root.keys, [5,6])
        self.assertListEqual(tree.root.values, [3,5])

        tree.insert(5, value=3)

        self.assertListEqual(tree.root.keys, [5,6])
        self.assertListEqual(tree.root.values, [3,5])

        tree.insert(10, value=1)

        self.assertListEqual(tree.root.keys, [5,6,10])
        self.assertListEqual(tree.root.values, [3,5,1])

    def test_repair_root(self):
        tree = btree.Tree(3)
        tree.root.keys = [1,2,3,4]
        tree.root.values = ['1','2','3','4']

        tree.repair(tree.root)




if __name__ == '__main__':
    unittest.main()
