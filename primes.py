"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes < 1:
    		raise ValueError('A very specific bad thing happened.')
    n = 3
    list.append(2)
    while len(list) < number_of_primes:
          count = 0
          for x in range(2, n):
              if n%x == 0:
                  count+=1
                  break
          if count == 0:
              list.append(n)
          n = n + 1
    return list

print(primes(20))
print(len(primes(20)))

print(primes(1))
