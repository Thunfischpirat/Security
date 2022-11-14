# Code for Sheet 1 exercise 2 a.
# @authors: Abdullah, Majdi, Christian.

from numbers import e, d, N, q, p

# Check whether N is the product of p and q.
print(f"N=p*q is {N == p * q}")

# Check whether e is the inverse of d modulo phi(N).
phi_N = (p - 1) * (q - 1)
print(f"d=e^-1 mod phi(N) is {d == pow(e, -1, phi_N)}")

# Therefore the given parameters don't form a valid RSA key pair.





