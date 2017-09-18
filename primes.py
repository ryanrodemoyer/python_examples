"""
some docstring
"""

def primes():
    """print all the prime numbers from 1..n"""
    upper_bound = 100

    for potential_prime in range(1, upper_bound):
        if (potential_prime == 1) or (potential_prime == 2) or (potential_prime == 3):
            print potential_prime
        else:
            is_prime = True

            for checker in range(2, potential_prime):
                if potential_prime % (checker) == 0:
                    is_prime = False
                    break

            if is_prime:
                print potential_prime

def my_method():
    """my_method doc string"""
    print "my name is ryan"

    input_text = input("enter a number")
    input_number = int(input_text)

    print input_number

primes()
