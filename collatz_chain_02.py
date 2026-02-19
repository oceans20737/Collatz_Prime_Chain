#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.
# https://opensource.org/licenses/MIT

from sympy import isprime

def is_collatz_prime_chain(start_val):
    """
    Generates a prime chain under the Collatz map f(x) = (3x + 1) / 2,
    starting from a given value. The chain continues as long as each
    term remains prime.

    Parameters:
        start_val (int): The starting value of the chain.

    Returns:
        list[int]: The list of consecutive primes in the chain.
    """
    chain = []
    current = start_val

    while isprime(current):
        chain.append(current)
        current = (3 * current + 1) // 2

    return chain

# Example: Display the discovered chain starting from 89599
if __name__ == "__main__":
    chain = is_collatz_prime_chain(89599)
    print(f"Collatz prime chain starting from 89599 (length {len(chain)}):")
    print(" → ".join(map(str, chain)))


# In[ ]:




