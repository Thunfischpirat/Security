# Code for Sheet 1 exercise 2 b.
# @authors: Abdullah, Majdi, Christian.
import hashlib

# Take the third root of c (Calculated with exact solver).
k = 27148856302067695012654929914525646859475523459929768303479760314974150236818
# Take SHA-256 of 271488 (first 6 digits of k).
m = hashlib.sha256(b"271488").hexdigest()
m_true = "b8786d97c2b37c92daa596ce93cb6970a0c3579a6f392d019f7124d25c97d99a"
# Check whether the hash is correct.
print(f"Hash is correct: {m == m_true}")
