
from functools import reduce

is_armstrong = lambda n: (lambda ls: reduce(lambda a, x: a + x**len(ls), ls))(list(map(int, str(n)))) == n

print(is_armstrong(153))
print(is_armstrong(10))