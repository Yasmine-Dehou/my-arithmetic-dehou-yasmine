def pgcd(a, b):
    """Calcul du pgcd de a et b"""
    while b:
        a, b = b, a % b
    return a