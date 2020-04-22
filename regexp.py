# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import re
from typing import List
from numbers import Number
import types

def regexp_0(text: str, pattern: str) -> List[slice]: #TODO тоже не очень поняла что подразумевалось под этим заданием и при чем тут slice
    res = re.finditer(pattern, text)
    list = []
    for i in res:
        list.append(slice(i.span()))
    
    return list
    """
    Finds the occurrence and position of the substrings within a string

    >>> regexp_0("LingvoX SpaceX SpacoX", "oX")
    [slice(5, 7, None), slice(19, 21, None)]
    """
    
def regexp_1(text: str) -> str:
    return re.sub(r'(?<!\b)(?=[A-Z])', '_', text).lower()
    """
    Converts camel case string to snake case string

    >>> regexp_1("QObject")
    'q_object'

    >>> regexp_1("KNeighborsClassifier")
    'k_neighbors_classifier'
    """
    
def regexp_2(text: str, length: int) -> str:
    return re.sub(r'(\b)(\w{3})(\b)', "", text)
    """
    Removes words from a string of length between 1 and a given number

    >>> regexp_2("Hello Cyril Kak dela bro", 3)
    'Hello Cyril dela'

    >>> regexp_2("Hello Cyril Kak dela bro", 4)
    'Hello Cyril'
    """  
    
def regexp_3(text: str) -> str:
    return re.sub(r' ?\(\w*\)', '', text)
    """
    Removes the parenthesis area in a string

    >>> regexp_3("Polina (Ivan)")
    'Polina'

    >>> regexp_3("Mark (Station) (LingvoX)")
    'Mark'
    """

def regexp_4(num: Number) -> bool:
    # res=re.split(r'\.', str(num))
    # if re.match(r'[0-9]*', res(0)) is not None:
        # if re.match(r'', res(1))
        
        
    if re.match(r'[0-9]*(\.[0-9]{1,2})?$', str(num)) is not None: return True
    else: return False
    """
    Returns true whenever a decimal with a precision of 2

    >>> regexp_4(1.22)
    True
    >>> regexp_4(1.2)
    True
    >>> regexp_4(11)
    True
    >>> regexp_4(11.)
    True
    >>> regexp_4(11.333)
    False
    """
    
#print(regexp_0("LingvoX SpaceX SpacoX", "oX"))
#print(regexp_1("QObject"))
#print(regexp_2("Hello Cyril Kak dela bro", 3))
#print(regexp_3("Polina (Ivan)"))
#print(regexp_3("Mark (Station) (LingvoX)"))
print(regexp_4(1.22))
print(regexp_4(1.2))
print(regexp_4(11))
print(regexp_4(11.))
print(regexp_4(11.333))