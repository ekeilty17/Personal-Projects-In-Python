from b_tree import *
from g_tree import *

def ConvertToBinaryTree_rec(g_tree, siblings):
    # Break case: at bottom of tree
    if g_tree == None:
        return None

    # init b_tree
    b_tree = binary_tree(g_tree.val)

    # if children, then we add the next successor to the left
    if g_tree.children != []:
        b_tree.left = ConvertToBinaryTree_rec(g_tree.children[0], g_tree.children[1:])

    # if siblings, then add them to the right
    if siblings != []:
        b_tree.right = ConvertToBinaryTree_rec(siblings[0], siblings[1:])

    return b_tree

def ConvertToBinaryTree(g_root):
    if g_root == None:
        return None
    return ConvertToBinaryTree_rec(g_root, [])


def ConvertToGeneralTree_rec(b_tree, g_tree):
    if b_tree == None:
        return False
    if g_tree == None:
        return False
    
    g_child = tree(b_tree.val)
    g_tree.AddSuccessor(g_child)

    if b_tree.left != None:
        ConvertToGeneralTree_rec(b_tree.left, g_child)
    if b_tree.right != None:
        ConvertToGeneralTree_rec(b_tree.right, g_tree)
    
    return True

def ConvertToGeneralTree(b_root):
    # Error cases
    if b_root == None:
        return None
    if b_root.right != None:
        return None
    g_root = tree(b_root.val)
    ConvertToGeneralTree_rec(b_root.left, g_root)
    return g_root
