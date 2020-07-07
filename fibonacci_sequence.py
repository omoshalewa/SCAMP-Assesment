# the function produces the output of a fibonacci sequence


def fib_seq(n):
    a = 0
    b = 1

    if n < 1:
        print(n)

    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)


# to print out a fibonacci sequence of 10 numbers
fib_seq(10)
