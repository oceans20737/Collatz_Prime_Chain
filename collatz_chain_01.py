#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.
# https://opensource.org/licenses/MIT

from sympy import isprime

def collatz_chain_search(limit, min_length=7):
    """
    Searches for prime chains under the Collatz map f(x) = (3x + 1) / 2.
    A chain is defined as a sequence of primes where each term is generated
    by applying f(x) to the previous one.
    
    Parameters:
        limit (int): Upper bound for the starting value x_0 (odd integers only).
        min_length (int): Minimum chain length to report.
    """
    for x in range(3, limit, 2):  # Only test odd starting values
        if not isprime(x):
            continue

        chain = [x]
        current = x

        while True:
            next_val = (3 * current + 1) // 2
            if isprime(next_val):
                chain.append(next_val)
                current = next_val
            else:
                # Optional: print reason for termination
                # print(f"Terminated at {next_val}, which is not prime.")
                break

        if len(chain) >= min_length:
            print(f"Length {len(chain)} chain found starting from {x}:")
            print(" → ".join(map(str, chain)))
            print()

# Example usage
if __name__ == "__main__":
    collatz_chain_search(limit=100000)


# In[ ]:




