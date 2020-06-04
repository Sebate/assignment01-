import tkinter as tk
from math import *


class Span:
    """
    Span objects are used to define boundaries within other iterables.
    """

    def __init__(self, start, end):
        if not start <= end:
            raise ValueError('Start cannot be greater than or equal to End')

        self._start = start
        self._end = end

    @property
    def span(self):
        """
        Return the span start and end scalars
        :return: The start and end indexes
        """
        return self._start, self._end

    def __eq__(self, other):
        start, fin = other.span()
        return self._start == start and self._end == fin


class DistanceCalculator:
    """
    The ADistanceCalculator class defines a metric on strings. It is a way of determining the distance from
    one string to another.
    """

    def __init__(self, insert_cost: object = 1, deletion_cost: object = 1, subst_cost: object = 1) -> object:
        """
        The constructor for the distance calculator. The insert, deletion, and substitution cost can be specified
        as state for the object.
        :param insert_cost:
        :param deletion_cost:
        :param subst_cost:
        """
        self._insert_cost = insert_cost
        self._deletion_cost = deletion_cost
        self._subst_cost = subst_cost

    def distance(self, source: object, target: object) -> object:

        if source == "":
            return len(target)
        if target == "":
            return len(source)
        if source[-1] == target[-1]:
            cost = 0
        else:
            cost = 1

        res = min([self.distance(source[:-1], target) + 1,
                   self.distance(source, target[:-1]) + 1,
                   self.distance(source[:-1], target[:-1]) + cost])

        return res




