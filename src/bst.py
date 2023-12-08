#!/usr/bin/env python3

from bt import BT
from sys import exit
from logging import getLogger, info

log = getLogger(__name__)


class BST(BT):
    def __init__(self, value=None):
        # Initializes an empty tree if `value` is None, else a root with the
        # specified `value` and two empty children.

        super().__init__(value)

        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        # Returns true if the value `v` is a member of the tree.

        info("TODO@src/bst.py: implement is_member()")
        return True if v in self.bfs_order_star() else False

    def size(self):
        # Returns the number of nodes in the tree.

        info("TODO@src/bst.py: implement size()")
        values = self.bfs_order_star()
        num_of_none_values = 0

        if len(values) == 0:
            return 0

        for val in values:
            if val is None:
                num_of_none_values += 1

        return len(values) - num_of_none_values

    def height(self):
        #  Returns the height of the tree.

        info("TODO@src/bst.py: implement height()")

        return 0 if self is None else 1 + max(self.get_lc().height(), self.get_rc().height())

    def preorder(self):
        #  Returns a list of all members in preorder.

        if self.is_empty():
            return []

        return [self.get_value()] + self.get_lc().preorder() + self.get_rc().preorder()

    def inorder(self):
        #  Returns a list of all members in inorder.
        log.info("TODO@src/bst.py: implement inorder()")
        if self.is_empty():
            return []

        return self.get_lc().inorder() + [self.get_value()] + self.get_rc().inorder()

    def postorder(self):
        # Returns a list of all members in postorder.
        log.info("TODO@src/bst.py: implement postorder()")

        if self.is_empty():
            return []

        return self.get_rc().postorder() + [self.get_value()] + self.get_lc().postorder()

    def bfs_order_star(self):
        # Returns a list of all members in breadth-first search* order, which
        # means that empty nodes are denoted by "stars" (here the value None).

        # For example, consider the following tree `t`:
        #            10
        #      5           15
        #   *     *     *     20

        # The output of t.bfs_order_star() should be:
        # [ 10, 5, 15, None, None, None, 20 ]

        log.info("TODO@src/bst.py: implement bfs_order_star()")

        if self.is_empty():
            return []

        queue = [self]
        values = []

        for i in range(2 ** self.height() - 1):
            cur_node = queue.pop()
            values.append(cur_node.get_value())

            queue.insert(0, self.get_lc())
            queue.insert(0, self.get_rc())

        return values

    def add(self, v):
        # Adds the value `v` and returns the new (updated) tree.  If `v` is
        # already a member, the same tree is returned without any modification.

        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.get_value():
            return self.cons(self.get_lc().add(v), self.get_rc())
        if v > self.get_value():
            return self.cons(self.get_lc(), self.get_rc().add(v))
        return self

    def delete(self, v):
        # Removes the value `v` from the tree and returns the new (updated) tree.
        # If `v` is a non-member, the same tree is returned without modification.

        if v is None:
            return self

        log.info("TODO@src/bst.py: implement delete()")
        return self


if __name__ == "__main__":
    log.critical("module contains no main module")
    exit(1)
