'''
Time Complexity: O(1) for all functions
Space COmplexity: O(1) for all functions
Run on Leetcode: YES
'''
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        if self.iterator.hasNext():
            self.curr = self.iterator.next()
        else:
            self.curr = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.curr
        

    def next(self):
        """
        :rtype: int
        """
        temp = self.curr
        if self.iterator.hasNext():
            self.curr = self.iterator.next()
        else:
            self.curr = None
        return temp
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curr != None