# -*- coding: utf-8 -*-

import re
from numbers import Number

def map_(func, iterable):
    for i in iterable:
        yield func(i)
    
    """
    The same as built-in map(), but generator

    >>> from collections import Generator
    >>> square = lambda x: x ** 2
    >>> isinstance(map_(square, range(10)), Generator)
    True
    >>> list(map_(square, range(10)))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """


def zip_(*iterables):
    
    i = iterables[0]
    j = iterables[1]
    k = iterables[2]   
    lenI = len(i)
    lenJ = len(j)
    lenK = len(k)
    
    f = 0
    if(lenI <= lenJ and lenI <= lenK):
        f = lenI
    elif (lenJ <= lenK): f = lenJ
    else: f = lenK
    
    res = []
    for ii in range(len(i)):
        yield [i[ii], j[ii], k[ii]]      
    """
    The same as built-in zip(), but generator

    >>> for i, j, k in zip_(range(3), range(4), range(-7, 0)):
    ...     print(i, j, k)
    0 0 -7
    1 1 -6
    2 2 -5

    """
    
def dropwhile(predicate, iterable):
    k = 0
    for i in iterable:
        if (predicate(i) and k == 0): continue
        elif (not predicate(i)): k += 1; yield i
        else: yield i
    
    """
    The same as itertools.dropwhile(), but generator

    >>> from collections import Generator
    >>> isinstance(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]), Generator)
    True
    >>> list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
    [6, 4, 1]
    """
    
def filterfalse(predicate, iterable):
    for i in iterable:
        if(not predicate(i)): yield i
    
    """
    The same as itertools.filterfalse(), but generator

    >>> from collections import Generator
    >>> isinstance(filterfalse(lambda x: x % 2, range(10)), Generator)
    True
    >>> list(filterfalse(lambda x: x % 2, range(10)))
    [0, 2, 4, 6, 8]
    """


def unique(iterable):
    res = []
    for i in iterable:
        if(i in res): continue
        else: res.append(i); yield i
    """
    Generates unique values from iterable object

    >>> from collections import Generator
    >>> isinstance(unique(range(10)), Generator)
    True
    >>> list(unique([1, 1, 2, 2, 3, 1, 11, -1]))
    [1, 2, 3, 11, -1]
    """
    
    
#import collections 
#from collections import Generator
square = lambda x: x ** 2
#print(isinstance(map_(square, range(10)), Generator)) TODO почему то с импортом не получилось, проверила иначе
import types
print(isinstance(map_(square, range(10)), types.GeneratorType))
print(list(map_(square, range(10))))
print('\n')

for i, j, k in zip_(range(3), range(4), range(-7, 0)):
    print(i, j, k)
    
print('\n')
print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))
print('\n')
print(list(filterfalse(lambda x: x % 2, range(10))))
print('\n')
print(list(unique([1, 1, 2, 2, 3, 1, 11, -1])))
