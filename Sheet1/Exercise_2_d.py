# Code for Sheet 1 exercise 2 d.
# @authors: Abdullah, Majdi, Christian.


class EllipticCurve:
    """
    Implementation of an elliptic curve in weierstrass normal form
    """
    def __init__(self, a: int, b: int, p: int):
        """
        Initialize an elliptic curve in weierstrass normal form

        Args:
            a: The coefficient of x in the equation of the curve.
            b: The coefficient of the constant term in the equation of the curve.
            p: The prime number that the curve is defined over.
        """
        # Check whether the curve is singular.
        if 4 * a**3 + 27 * b**2 == 0:
            raise ValueError("The given parameters don't form a valid elliptic curve.")
        self.a = a
        self.b = b
        self.p = p

    def __repr__(self):
        """ Return a string representation of the curve. """
        return f"y^2 = x^3 + {self.a}x + {self.b} (mod {self.p})"

    def __contains__(self, point):
        """ Check whether a point is on the curve. """
        x, y = point
        return (y**2 - x**3 - self.a * x - self.b) % self.p == 0

    def add(self, point1, point2):
        """
        Add two points on the curve.
        """
        if point1 not in self:
            raise ValueError("The first point is not on the curve.")
        if point2 not in self:
            raise ValueError("The second point is not on the curve.")
        x1, y1 = point1
        x2, y2 = point2
        if point1 == point2:
            s = (3 * x1**2 + self.a) * pow(2 * y1, -1, self.p)
        else:
            s = (y2 - y1) * pow(x2 - x1, -1, self.p)
        x3 = s**2 - x1 - x2
        y3 = s * (x1 - x3) - y1
        return x3 % self.p, y3 % self.p

    def mul(self, point, n):
        """
        Multiply a point on the curve with a scalar.
        """
        if point not in self:
            raise ValueError("The point is not on the curve.")
        result = point
        for _ in range(n - 1):
            result = self.add(result, point)
        return result

if __name__ == "__main__":
    # Parameters for the elliptic curve.
    d = 5
    P = (3, 1)
    # Create the elliptic curve.
    E = EllipticCurve(2, 2, 17)
    # Calculate T.
    T = E.mul(P, d)
    print(f"T = {T}")