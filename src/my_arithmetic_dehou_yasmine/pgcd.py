def pgcd(a, b):
    """
    Compute the greatest common divisor (GCD) of two numbers.

    Parameters
    ----------
    a : int
        First number.
    b : int
        Second number.

    Returns
    -------
    int
        The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a