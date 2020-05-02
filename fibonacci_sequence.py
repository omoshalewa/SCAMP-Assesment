# the function produces the output of a fibonacci sequence


def fib_seq(n):
    a = 1
    b = 2

    if n == 1:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(a + b)


# to print out a fibonacci sequence of 10 numbers
fib_seq(10)
