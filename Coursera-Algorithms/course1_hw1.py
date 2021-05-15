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
    x_0 = _a % 100
    y_0 = _b % 100
    x_1 = (_a - x_0) / 100
    y_1 = (_b - y_0) / 100
    z_2 = x_1 * y_1
    z_1 = x_1 * y_0 + x_0 * y_1
    z_0 = x_0 * y_0
    return int(z_2 * (100 ** 2) + z_1 * 100 + z_0)

NUM1 = 3141592653589793238462643383279502884197169399375105820974944592
NUM2 = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(NUM1, NUM2))
