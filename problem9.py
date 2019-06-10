
from functools import reduce


def prob9():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    SUMM = 1000
    return \
        [a * b * (SUMM - a - b) for a in range(1, SUMM) for b in range(a, SUMM) if a ** 2 + b ** 2 ==
         (SUMM - a - b) ** 2][0]


def prob6(n: int):
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the
    sum is 3025 − 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural
    numbers and the square of the sum.
    """
    return sum(range(n + 1)) ** 2 - sum([i ** 2 for i in range(1, n + 1)])


def prob48(n: int):
    """
    The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
    Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
    """
    return sum([i**i for i in range(1, n+1)]) % 10**10


def prob40_reduce():
    """
    An irrational decimal fraction is created by concatenating the positive integers:
    0.123456789101112131415161718192021...
    It can be seen that the 12th digit of the fractional part is 1.
    If dn represents the nth digit of the fractional part, find the value of the following expression.
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

    eq procedure solution - prob40()
    """
    positions = list(map(lambda i: 10**i - reduce(lambda a, x: x + a, list(map(lambda k: 9 * k * 10**(k-1), range(1,i)))), range(2, 7))) # returne numbers in
    res = reduce(lambda x, a: a*x,
                  [int
                   (str(position_i // (i + 2) + 10**(i+1) - int((lambda x, i: x % (i+2) == 0)(position_i, i)))
                    [position_i % (i+2)-1 + int((lambda x, i: x % (i+2) == 0)(position_i, i))])
                   for i, position_i in enumerate(positions)])
    return res


print('problem 9:', prob9())
print('problem 6:', prob6(100))
print('problem 48:', prob48(1000))
print('problem 40:', prob40_reduce())


# def prob40(n: int):
#     k = 1
#     s = 9
#
#     while n > s:
#         k += 1
#         s += k * 9 * 10**(k-1)
#     else:
#         if (n - (s - k * 9 * 10**(k-1))) % k - 1:
#             return str((n - (s - k * 9 * 10**(k-1))) // k + 10**(k-1))[(n - (s - k * 9 * 10**(k-1))) % k -1]
#         else:
#             return str((n - (s - k * 9 * 10**(k-1))) // k + 10**(k-1) - 1)[0]
#
#
