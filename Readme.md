# priorityq
## An object-oriented priority queue with updatable priorities.

The priorityq package provides a `MappedQueue` class implementing an
efficient minimum heap. The smallest element can be popped in O(1) time, new
elements can be pushed in O(log n) time, and any element can be removed or
updated in O(log n) time. The queue cannot contain duplicate elements and an
attempt to push an element already in the queue will have no effect.

`MappedQueue` complements the heapq package from the python standard library,
and has slightly different functionality. While `MappedQueue` is designed for
maximum compatibility with heapq, it is an independent implementation. The
priorityq package is free and open-source software and is released under
multiple licenses (see LICENSE for more info).

## Usage
A `MappedQueue` can be created empty or optionally given an array of initial
elements. Calling `push()` will add an element and calling `pop()` will remove
and return the smallest element.

    >>> q = MappedQueue([916, 50, 4609, 493, 237])
    >>> q.push(1310)
    True
    >>> x = [q.pop() for i in range(len(q.h))]
    >>> x
    [50, 237, 493, 916, 1310, 4609]



