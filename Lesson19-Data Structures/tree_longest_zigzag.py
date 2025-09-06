# Data Structures / TreeLongestZigZag

# Given a tree, find a downward path with the maximal number of direction changes.

'''
In this problem we consider binary trees. Let's define a turn on a path as a change in the direction of the path (i.e. a switch from right to left or vice versa). A zigzag is simply a sequence of turns (it can start with either right or left). The length of a zigzag is equal to the number of turns.

Consider binary tree below:



There are two turns on the marked path. The first one is at [15]; the second is at [30]. That means that the length of this zigzag is equal to 2. This is also the longest zigzag in the tree under consideration. In this problem you should find the longest zigzag that starts at the root of any given binary tree and form a downwards path.

Note that a zigzag containing only one edge or one node has length 0.

Problem
Write a function:

def solution(T)

that, given a non-empty binary tree T consisting of N nodes, returns the length of the longest zigzag starting at the root.

For example, given tree T shown in the figure above, the function should return 2, as explained above. Note that the values contained in the nodes are not relevant in this task.

Technical details
A binary tree can be specified using a pointer data structure. Assume that the following declarations are given:

from dataclasses import dataclass, field

@dataclass
class Tree:
    x: int = 0
    l: "Tree" = None
    r: "Tree" = None

An empty tree is represented by an empty pointer (denoted by None). A non-empty tree is represented by a pointer to an object representing its root. The attribute x holds the integer contained in the root, whereas attributes l and r hold the left and right subtrees of the binary tree, respectively.

For the purpose of entering your own test cases, you can denote a tree recursively in the following way. An empty binary tree is denoted by None. A non-empty tree is denoted as (X, L, R), where X is the value contained in the root and L and R denote the left and right subtrees, respectively. The tree from the above figure can be denoted as:

  (5, (3, (20, (6, None, None), None), None), (10, (1, None, None), (15, (30, None, (9, None, None)), (8, None, None))))
Assumptions
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
the height of tree T (number of edges on the longest path from root to leaf) is within the range [0..800].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task
from dataclasses import dataclass
from typing import Optional

@dataclass
class Tree:
    x: int = 0
    l: Optional["Tree"] = None
    r: Optional["Tree"] = None

def solution(T: Optional[Tree]) -> int:
    max_turns = 0

    def dfs(node, is_left, turns):
        nonlocal max_turns
        if not node:
            return
        max_turns = max(max_turns, turns)
        if is_left:
            # Change direction: go right (this is a turn)
            dfs(node.r, False, turns + 1)
            # Same direction: go left (no turn, reset)
            dfs(node.l, True, 0)
        else:
            # Change direction: go left (this is a turn)
            dfs(node.l, True, turns + 1)
            # Same direction: go right (no turn, reset)
            dfs(node.r, False, 0)

    # Start from root, try both directions
    if T.l:
        dfs(T.l, True, 0)
    if T.r:
        dfs(T.r, False, 0)

    return max_turns
