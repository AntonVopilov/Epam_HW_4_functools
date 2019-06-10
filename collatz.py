
def collatz_steps(n: int):
    def recur(n, counter=None):
        counter = counter or 0
        counter += 1
        if n == 1:
            return counter - 1
        else:
            make_step = lambda n: n//2 * int((lambda a: a % 2 == 0)(n)) + (3 * n + 1) * int((lambda a: a % 2 != 0)(n))
            return recur(make_step(n), counter)
    return recur(n)


print(collatz_steps(44))

def collatz(n):
    make_step = lambda val,counter: counter if val == 1 else make_step(val/2, counter + 1) if val % 2 == 0 \
        else make_step(val*3 + 1, counter + 1)
    return make_step(n,0)

print(collatz(44))