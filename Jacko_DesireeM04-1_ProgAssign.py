def isPrime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def displayPrimes(num):
    """Display all prime numbers up to num."""
    primes = [i for i in range(2, num + 1) if isPrime(i)]
    for prime in primes:
        print(prime)

def main():
    try:
        num = int(input("Enter an integer greater than 1: "))
        if num <= 1:
            print("Please enter a number greater than 1.")
        else:
            displayPrimes(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

main()

