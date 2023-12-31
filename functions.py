# testproject
def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    elif number <= 3:
        return True   # 2 and 3 are prime
    elif number % 2 == 0 or number % 3 == 0:
        return False  # Multiples of 2 and 3 are not prime

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False  # If divisible by i or i + 2, not prime
        i += 6  # Increment by 6 to check numbers of the form 6k ± 1

    return True

# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is prime and display the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
