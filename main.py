import numpy

# 1/(sqrt(1+x)). a = -0.1, b = 1;
a = float(input("Enter an a:"))
b = float(input("Enter a b:"))
e = float(input("Enter an e:"))



def f20_1(x: float) -> float:
    return 1 / numpy.sqrt(1 + x)


def f20_2(x: float, e: float):
    s = 1.0
    term = 1.0
    iterations = 0.0
    while numpy.abs(term) > e:
        term = x*((1/2)-(1/(iterations+1)))
        iterations += 1.0
        s += term
    return [s, iterations]


step = (b - a) / 10.0
x = a
print("x      |  f1(x)        |  f2(X)        | precision |  iterations")
while x <= b:
    precision = numpy.abs(f20_2(x, e)[0] - f20_1(x))
    print(format(x, ".3f") + "  |  " + format(f20_1(x), ".9f") + "  |  " + format(f20_2(x, e)[0], ".9f") + "  |  " +
          format(precision, ".5f") + "  |  " + format(f20_2(x, e)[1], ".3f"))
    x += step
