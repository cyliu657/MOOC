'''
To get the most out of this assignment,
your program should restrict itself to multiplying only pairs of single-digit numbers.
You can implement the grade-school algorithm if you want,
but to get the most out of the assignment you'll want to
implement recursive integer multiplication and/or Karatsuba's algorithm.
'''

def karatsuba(_a, _b):
    '''
    Run Karatsuba algorithms
    :param _a: an integer
    :param _b: an integer
    :return: multiplication of a and b
    '''
    if len(str(_a)) == 1 or len(str(_b)) == 1:
        return _a * _b
    else:
        n = max(len(str(_a)), len(str(_b)))
        base = n // 2

        a = _a // 10 ** (base)
        b = _a % 10 ** (base)
        c = _b // 10 ** (base)
        d = _b % 10 ** (base)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_bc = karatsuba(a+b, c+d) - ac - bd

        prod = ac * 10 ** (2*base) + (ad_bc * 10 ** base) + bd
        return prod

NUM1 = 3141592653589793238462643383279502884197169399375105820974944592
NUM2 = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(NUM1, NUM2))
