# add a new test
# check if fails
# makeit pass (with the others)
# refactor (if needed)
# go to 1

import pytest
import numpy as np

class Fraction(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.reduced_from = f'{self.a}/{self.b}'
        self.test = 0

    def next_test(self):
        self.test += 1

    def get_reduced_form(self):
        """return the reduced form of the fraction a/b"""
        gcd = np.gcd(self.a, self.b)
        if self.reduced_from != f'{self.a//gcd}/{self.b//gcd}':
            self.reduced_from = f'{self.a//gcd}/{self.b//gcd}'

    def check(self):
        if self.test == 0:
            if self.b != 0:
                return 'No Division by zero error'

        if self.test == 1:
            if isinstance(self.a, int) and isinstance(self.b, int):
                return 'a and b are integers'

        if self.test == 2:
            gcd = np.gcd(self.a, self.b)
            if self.reduced_from == f'{self.a//gcd}/{self.b//gcd}':
                return 'Fraction is in its reduced form'

        if self.test == 3:
            if np.sign(self.b) != -1:
                return 'b is not negative'



def test_division_possibility():
    frac = Fraction(1, 1)
    assert frac.check() == 'No Division by zero error'

def test_integer_form():
    frac = Fraction(3, 9)
    frac.check()
    frac.next_test()
    assert frac.check() == 'a and b are integers'  

def test_reduced_from():
    frac = Fraction(1, 3)
    frac.check()
    frac.next_test()
    frac.check()  
    frac.next_test()
    assert frac.check() == 'Fraction is in its reduced form'

def test_b_is_not_negative():
    frac = Fraction(1, 3)
    frac.check()
    frac.next_test()
    frac.check()  
    frac.next_test()
    frac.check()
    frac.next_test()
    assert frac.check() == 'b is not negative'
