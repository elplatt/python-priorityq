# -*- coding: utf-8 -*-
#
# priorityq: An object-oriented priority queue with updatable priorities.
#
# Copyright 2018 Edward L. Platt
#
# This software is released under multiple licenses. See the LICENSE file for
# more information.
#
# Authors:
#   Edward L. Platt <ed@elplatt.com>
"""Priority queue class with updatable priorities.
"""

import heapq

__all__ = ['MappedQueue']

class MappedQueue(object):
    """Class encapsulating a priority queue implemented as a mapped heap.
    """
    
    def __init__(self, data=[]):
        """Priority queue class with updatable priorities.
        """
        self.h = list(data)
        self.d = dict()
        self._heapify()
    
    def _heapify(self):
        """Restore heap invariant and recalculate map."""
        heapq.heapify(self.h)
        self.d = dict([(elt, pos) for pos, elt in enumerate(self.h)])
        if len(self.h) != len(self.d):
            raise AssertionError("Heap contains duplicate elements")
    
    def push(self, elt):
        """Add an element to the queue."""
        # If element is already in queue, do nothing
        if elt in self.d:
            return False
        # Add element to heap and dict
        pos = len(self.h)
        self.h.append(elt)
        self.d[elt] = pos
        # Restore invariant by sifting down
        self._siftdown(pos)
        return True
    
    def pop(self):
        """Remove and return the smallest element in the queue."""
        # Remove smallest element
        elt = self.h[0]
        del self.d[elt]
        # If elt is last item, remove and return
        if len(self.h) == 1:
            self.h.pop()
            return elt
        # Replace root with last element
        last = self.h.pop()
        self.h[0] = last
        self.d[last] = 0
        # Restore invariant by sifting up, then down
        pos = self._siftup(0)
        self._siftdown(pos)
        # Return smallest element
        return elt
    
    def update(self, elt, new):
        """Replace an element in the queue with a new one."""
        # Replace
        pos = self.d[elt]
        self.h[pos] = new
        del self.d[elt]
        self.d[new] = pos
        # Restore invariant by sifting up, then down
        pos = self._siftup(pos)
        self._siftdown(pos)
        
    def remove(self, elt):
        """Remove an element from the queue."""
        # Find and remove element
        try:
            pos = self.d[elt]
            del self.d[elt]
        except KeyError:
            # Not in queue
            raise
        # If elt is last item, remove and return
        if pos == len(self.h) - 1:
            self.h.pop()
            return
        # Replace elt with last element
        last = self.h.pop()
        self.h[pos] = last
        self.d[last] = pos
        print(self.h)
        # Restore invariant by sifting up, then down
        pos = self._siftup(pos)
        print(self.h)
        self._siftdown(pos)
        print(self.h)
            
    def _siftup(self, pos):
        """Move element at pos down to a leaf by repeatedly moving the smaller
        child up."""
        h, d = self.h, self.d
        elt = h[pos]
        # Continue until element is in a leaf
        end_pos = len(h)
        left_pos = (pos << 1) + 1
        while left_pos < end_pos:
            # Left child is guaranteed to exist by loop predicate
            left = h[left_pos]
            try:
                right_pos = left_pos + 1
                right = h[right_pos]
                # Out-of-place, swap with left unless right is smaller
                if right < left:
                    h[pos], h[right_pos] = right, elt
                    pos, right_pos = right_pos, pos
                    d[elt], d[right] = pos, right_pos
                else:
                    h[pos], h[left_pos] = left, elt
                    pos, left_pos = left_pos, pos
                    d[elt], d[left] = pos, left_pos
            except IndexError:
                # Left leaf is the end of the heap, swap
                h[pos], h[left_pos] = left, elt
                pos, left_pos = left_pos, pos
                d[elt], d[left] = pos, left_pos
            # Update left_pos
            left_pos = (pos << 1) + 1
        return pos
            
    def _siftdown(self, pos):
        """Restore invariant by repeatedly replacing out-of-place element with
        its parent."""
        h, d = self.h, self.d
        elt = h[pos]
        # Continue until element is at root
        while pos > 0:
            parent_pos = (pos - 1) >> 1
            parent = h[parent_pos]
            if parent > elt:
                # Swap out-of-place element with parent
                h[parent_pos], h[pos] = elt, parent
                parent_pos, pos = pos, parent_pos
                d[elt] = pos
                d[parent] = parent_pos
            else:
                # Invariant is satisfied
                break
        return pos
    