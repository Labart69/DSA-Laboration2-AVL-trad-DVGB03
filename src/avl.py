#!/usr/bin/env python3

from sys import exit
from bst import BST
from logging import getLogger

log = getLogger(__name__)


class AVL(BST):
    def __init__(self, value=None):
        # Initializes an empty tree if `value` is None, else a root with the
        # specified `value` and two empty children.

        super().__init__()
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def balance_factor(self):
        return self.get_lc().height() - self.get_rc().height()

    def add(self, v):

        # Example which shows how to override and call parent methods.  You
        # may remove this function and override something else if you'd like.

        log.debug("calling bst.BST.add() explicitly from child")
        # TODO: apply balance() correctly for add/delete
        return super().add(v)

    def balance(self):
        # AVL-balances around the node rooted at `self`.  In other words, this
        # method applies one of the following if necessary: slr, srr, dlr, drr.

        log.info("TODO@src/avl.py: implement balance()")

        return self

    def slr(self):
        # Performs a single-left rotate around the node rooted at `self`.

        n = self.get_rc()
        self.set_rc(None)
        n.set_lc(self)

        log.info("TODO@src/avl.py: implement slr()")
        return n

    def srr(self):
        # Performs a single-right rotate around the node rooted at `self`.

        n = self.get_lc()
        self.set_lc(None)
        n.set_rc(self)

        log.info("TODO@src/avl.py: implement srr()")
        return n

    def dlr(self):

        # Performs a double-left rotate around the node rooted at `self`.

        log.info("TODO@src/avl.py: implement drl()")
        return self

    def drr(self):
        # Performs a double-right rotate around the node rooted at `self`.

        log.info("TODO@src/avl.py: implement drr()")
        return self


if __name__ == "__main__":
    log.critical("module contains no main module")
    exit(1)
