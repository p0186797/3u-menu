import doctest

def gcd(m, n):
    """(int) -> int
    Returns the greatest common divisor between positive integers m and n.
    >>> gcd(2,6)
    2
    >>> gcd(24, 72)
    24
    >>> gcd(50, 60)
    10
    """

    #  initialize d to be min of m and n
    d = min(m,n)
    #  while d is not a factor of both
    while m % d !=0 or n % d != 0:
        #  decrease d by 1
        d -= 1
    return d

def reduce_fraction(m, n):
    d = gcd(m, n)
    m = m // d
    n = n // d
    return m, n

if __name__ == "__main__":
    doctest.testmod()
    assert gcd(108,81) == 27
    assert gcd(12, 24) == 12
    assert gcd(1, 6) == 1
    assert reduce_fraction(12, 24) == (1, 2)
