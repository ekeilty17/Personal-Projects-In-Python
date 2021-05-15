from tree import Tree
from binary_tree import BinaryTree

def ConvertToBinaryTree(g_tree, siblings=[]):
    # Break case: at bottom of Tree
    if g_tree == None:
        return None

    # init b_tree
    b_tree = BinaryTree(g_tree.val)

    # if children, then we add the next successor to the left
    if g_tree.children != []:
        b_tree.left = ConvertToBinaryTree(g_tree.children[0], g_tree.children[1:])

    # if siblings, then add them to the right
    if siblings != []:
        b_tree.right = ConvertToBinaryTree(siblings[0], siblings[1:])

    return b_tree

def _ConvertToGeneralTree_rec(b_tree, g_tree):
    if b_tree == None:
        return None
    if g_tree == None:
        return None
    
    g_child = Tree(b_tree.val)
    g_tree.add_successor(g_child)

    if b_tree.left != None:
        _ConvertToGeneralTree_rec(b_tree.left, g_child)
    if b_tree.right != None:
        _ConvertToGeneralTree_rec(b_tree.right, g_tree)

def ConvertToGeneralTree(b_root):
    # Error cases
    if b_root == None:
        return None
    if b_root.right != None:
        return None
    g_root = Tree(b_root.val)
    _ConvertToGeneralTree_rec(b_root.left, g_root)
    return g_root

if __name__ == "__main__":

    # Making General Tree
    g_root = Tree(1000)
    y = Tree(2000)
    z = Tree(3000)
    c = Tree(5)
    d = Tree(6)
    e = Tree(10)
    f = Tree(11)
    g = Tree(120)
    h = Tree(1234)

    g_root.add_successor(y)
    g_root.add_successor(f)
    g_root.add_successor(g)

    y.add_successor(d)
    y.add_successor(z)
    y.add_successor(e)

    z.add_successor(c)

    g.add_successor(h)

    print "Original General Tree"
    print g_root
    print

    g_to_b = ConvertToBinaryTree(g_root)
    print "Converted Binary Tree"
    print g_to_b
    print

    back_to_g = ConvertToGeneralTree(g_to_b)
    print "Converted Back to General Tree"
    print back_to_g
    print


    print "__________________________________"
    print

    # Making Binary Tree
    b_root = BinaryTree(10000)
    b_root.add_in_order([100, 500, -5, 10, 1, -10, 50, 3, 90, 0])

    print "Original Binary Tree"
    print b_root
    print

    b_to_g = ConvertToGeneralTree(b_root)
    print "Converted to General Tree"
    print b_to_g
    print

    back_to_b = ConvertToBinaryTree(b_to_g)
    print "Converted Back to Binary Tree"
    print back_to_b
    print