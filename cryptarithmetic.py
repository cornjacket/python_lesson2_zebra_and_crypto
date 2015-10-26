# -------------
# User Instructions
#
# Write a function, solve(formula) that solves cryptarithmetic puzzles.
# The input should be a formula like 'ODD + ODD == EVEN', and the 
# output should be a string with the digits filled in, or None if the
# problem is not solvable.
#
# Note that you will not be able to run your code yet since the 
# program is incomplete. Please SUBMIT to see if you are correct.

import string, re 
import itertools

import time

# taken from zebra_puzzle.py
def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    # Your code here
    for filling in fill_in(formula):
        if valid(filling): return filling
    return None # None is automatically returned so line not needed.
        
# assume: def fill_in(formula):
#        "Generate all possible fillings-in of letters in formula with digits."

def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall('[A-Z]',formula))) #should be a string
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def my_fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    regex = re.compile('[^a-zA-Z]') # but should only use caps
    letters = ''.join(set(regex.sub('',formula))) #should be a string
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

def tinkering():
    # tinkering with removing multiple characters
    print ''.join(set('aaabcabccd'))

    # tinkering with keeping only alphabetic characters
    regex = re.compile('[^a-zA-Z]')
    print regex.sub('','ab3d*Ed')

    my_input = 'A+B==C'
    print ''.join(set(regex.sub('',my_input)))

    formula = 'A+B=C'
    regex = re.compile('[^a-zA-Z]')
    letters = ''.join(set(regex.sub('',formula))) #should be a string
    print letters

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N < 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()

def test():
    t0 = time.clock()
    for example in examples:
        print; print 13*' ', example
        print '%6.4f sec:    %s ' % timedcall(solve, example)
    print '%6.4f tot.' % (time.clock()-t0)

#import cProfile
#cProfile.run('tinkering()')

# compile word is for optimized solution
def my_compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    # if not lower case
    if not word.isupper(): return word
    result = '('
    power = 1 # idx, val in enumerate(ints):
    for idx,digit in enumerate(reversed(word)):
        if idx != 0:
            result += ' + '
        result += str(power)+'*'+digit
        power *= 10
    result += ')'
    return result

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    # if not lower case
    if word.isupper():
        terms = [('%s*%s' % (10**i,d))
                 for (i,d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

print compile_word("HELLO")
print compile_word("H")
print compile_word("and")

word = "ALL"
if all(c.isupper() for c in word): print word

word = "AnL"
if all(c.isupper() for c in word): print word

test()
