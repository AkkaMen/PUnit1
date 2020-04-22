# -*- coding: utf-8 -*-
import re
from numbers import Number
import math



def register_count(string):
    l=0
    u=0
    for c in string:
        if c.isalpha():
            if c.islower(): l = l + 1 
            else: u = u + 1
    print('UPPER: {}, LOWER: {}'.format(u, l))
    
    """
    :param string: str, input string
    :return: dict, dict of lower and upper letter counts

    >>> register_count("Mama") == {'UPPER': 1, 'LOWER': 3}
    True
    >>> register_count("Your Name") == {'UPPER': 2, 'LOWER': 6}
    True
    >>> register_count("LingvoX!!!") == {'UPPER': 2, 'LOWER': 5}
    True
    >>> register_count("Trud, mir, mai! Zvahka!") == {'UPPER': 2, 'LOWER': 14}
    True
    >>> register_count("Coi ZIV!,,,,,") == {'UPPER': 4, 'LOWER': 2}
    True
    """


def pairwise_diff(first, second):
    p = 0.0
    if (len(first) == len(second)):
        for i in range(len(first)):
            if(first[i] <> second[i]): p = p + 1
        return round(100.0/(len(first)/p)/100.0, 2)
        
    else: raise AssertionError("most recent call last")
    
    
    
    """
    :param first: str, first input string
    :param second: str, second input string
    :return: float, percentage of different letters
 
    >>> pairwise_diff('ABSD', 'ABCD')
    0.25
    >>> pairwise_diff('aBSD', 'ABCD')
    0.5
    >>> pairwise_diff('LingvX', 'SpaceX')
    0.83
    >>> pairwise_diff('LingvoX', 'SpaceX')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> pairwise_diff('abc', 'ab')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> first = 'Salaman..'; second = 'Salaman.!'
    >>> round(1. / len(first), 2) == pairwise_diff(first, second)
    True
    >>> pairwise_diff(first + second, first + first)
    0.06
    >>> pairwise_diff(first * 3, second * 2 + first)
    0.07
    """


def run_robot():
    """
    Uses input() inside.
    :return: int, rounded euclidean distance from origin
    """
    print('Input a: ')
    a = input()
    print('Input b: ')
    b = input()
    print('Input x: ')
    x = input()
    print('Input y: ')
    y = input()
    print("\n")
    res = math.sqrt((x - a)*(x - a) + (y - b)*(y - b))
    print(round(res, 2))
    
    
def divisible(begin, end): #TODO вообще не смогла разгадать смысл задания, так что сделала как поняла
    nums = []
    for i in range(begin, end):
        if (i % 7 == 0): nums.append(str(i))
        
    return ' '.join(nums)
    
    """
    
    :param begin: int, positive integer
    :param end: int, positive integer
    :return: str, string of space separated integers

    Examples of usage:
    >>> divisible(1, 10)
    '7'
    >>> divisible(1, 17)
    '7 14'
    >>> len(divisible(100, 1000))
    407
    >>> divisible(29, 60)
    '42 49 56'
    >>> len(divisible(300, 3000).split())
    309
    >>> ns = [int(n) for n in divisible(300, 10000).split()]
    >>> seven_mask = [not bool(n % 7) for n in ns]
    >>> all(seven_mask)
    True
    >>> any(seven_mask)
    True
    >>> five_mask = [not bool(n % 5) for n in ns]
    >>> all(five_mask)
    False
    >>> any(five_mask)
    False
    >>> divisible(2, 5)
    ''
    >>> 1329 not in ns
    True
    """
    
    
    
print(divisible(1, 10))
print(divisible(1, 17))
print(len(divisible(100, 1000)))
print(divisible(29, 60))
print(len(divisible(300, 3000).split()))
ns = [int(n) for n in divisible(300, 10000).split()]
seven_mask = [not bool(n % 7) for n in ns]
print(all(seven_mask))
print(any(seven_mask))
five_mask = [not bool(n % 5) for n in ns]
print(all(five_mask))
print(any(five_mask))
print(1329 not in ns)
run_robot()
register_count("Mama")
register_count("Your Name")
register_count("LingvoX!!!")
register_count("Trud, mir, mai! Zvahka!")
register_count("Coi ZIV!,,,,,")
print("\n")
print(pairwise_diff('ABSD', 'ABCD'))
print(pairwise_diff('aBSD', 'ABCD'))
print(pairwise_diff('LingvX', 'SpaceX'))
first = 'Salaman..'; second = 'Salaman.!'
print(pairwise_diff('Salaman..' * 3, 'Salaman.!' * 2 + 'Salaman..'))
print(round(1. / len(first), 2) == pairwise_diff(first, second))
print(pairwise_diff(first + second, first + first))
print(pairwise_diff(first * 3, second * 2 + first))
print("\n")