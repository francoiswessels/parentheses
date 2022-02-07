from ast import expr_context
from multiprocessing.sharedctypes import Value
from turtle import st
from typing import List
from collections import deque

from pandas_datareader import test



OPENERS = {'(', '{'}
CLOSERS = {')', '}'}
PAIRS = {')':'(', '}':'{'}

assert len(OPENERS) == len(CLOSERS), \
    '''Opening and closing sets are mismatched in length. This is a packaging 
    failure. Please contact module developer.'''

assert set(CLOSERS) == set(PAIRS.keys()), \
    '''Parenthesis pairs are mismatched with the closing set. This is a packaging 
    failure. Please contact module developer.'''


class ParenthesisError(Exception):
    pass


def parse(test_variable: List[str]) -> int:
    # In theory deque is faster than list here though I have not tested it myself.
    # https://realpython.com/how-to-implement-python-stack/#using-collectionsdeque-to-create-a-python-stack
    stack = deque()
    for var in test_variable:
        if var in OPENERS:
            stack.append(var)
        elif var in CLOSERS:
            if len(stack) == 0:
                raise ParenthesisError(f"Imbalanced parenthesis found.")
            prev = stack.pop()
            if not prev == PAIRS[var]:
                raise ParenthesisError(f"Mismatched closing parenthesis found. '{prev}' does not match {var}!")
        else:
            raise ParenthesisError(f"This function can only handle known parentheses, not '{var}'")
    
    if not len(stack) == 0:
        raise ParenthesisError(f"Imbalanced parenthesis found.")
    
    return 0


def balanced(test_variable: List, start_index:int = 0, current_index:int = 0) -> bool:
    try:
        outcome = parse(test_variable)
    except ParenthesisError as ex:
        return False
    return outcome == 0