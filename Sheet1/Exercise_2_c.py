# Code for Sheet 1 exercise 2 c.
# @authors: Abdullah, Majdi, Christian.

from numbers import e_c as e
from numbers import N_c as N
from numbers import m, s

# Create a new valid signature by taking the fifth power of s modulo N.
s_hat = pow(s, 5, N)
print(f"New signature is {s_hat}.")
# Check whether the signature is valid.
m_hat = pow(m, 5)
print(f"Signature is valid: {pow(s_hat, e, N) == m_hat}")