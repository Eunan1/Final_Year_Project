import random

def calculate_modulus(N):
    # Generate a random number x between 1 and 99
    x = random.randint(1, 99)
    
    # Calculate y = x^2 mod N
    y = (x ** 2) % N
    
    return x, y

# Example usage, with N = 10
N = random.randint(1, 99)
x, y = calculate_modulus(N)
x, y