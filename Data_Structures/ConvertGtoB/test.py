"""
ConvertToGeneralTree is returning None, figure that out
"""

from b_tree import *
from g_tree import *
from convert import *

# Making General Tree
g_root = tree(1000)
y = tree(2000)
z = tree(3000)
c = tree(5)
d = tree(6)
e = tree(10)
f = tree(11)
g = tree(120)
h = tree(1234)


g_root.AddSuccessor(y)
g_root.AddSuccessor(f)
g_root.AddSuccessor(g)

y.AddSuccessor(d)
y.AddSuccessor(z)
y.AddSuccessor(e)

z.AddSuccessor(c)

g.AddSuccessor(h)

print "Original General Tree"
g_root.DepthFirst_style()
print

g_to_b = ConvertToBinaryTree(g_root)
print "Converted Binary Tree"
g_to_b.Print_DepthFirst()
print

back_to_g = ConvertToGeneralTree(g_to_b)
print "Converted Back to General Tree"
back_to_g.DepthFirst_style()
print


print "__________________________________"
print

# Making Binary Tree

b_root = binary_tree(10000)
b_root.Add_in_order(100)
b_root.Add_in_order(500)
b_root.Add_in_order(-5)
b_root.Add_in_order(10)
b_root.Add_in_order(1)
b_root.Add_in_order(-10)
b_root.Add_in_order(50)
b_root.Add_in_order(3)
b_root.Add_in_order(90)
b_root.Add_in_order(0)

print "Original Binary Tree"
b_root.Print_DepthFirst()
print

b_to_g = ConvertToGeneralTree(b_root)
print "Converted to General Tree"
b_to_g.DepthFirst_style()
print

back_to_b = ConvertToBinaryTree(b_to_g)
print "Converted Back to Binary Tree"
back_to_b.Print_DepthFirst()
print
