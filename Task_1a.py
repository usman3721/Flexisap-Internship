# def is_prime(num):
#   """Checks if a given number is prime.

#   Args:
#       num (int): The number to check for primality.

#   Returns:
#       bool: True if the number is prime, False otherwise.
#   """

#   if num <= 1:
#     return False
#   if num <= 3:
#     return True
#   if num % 2 == 0 or num % 3 == 0:
#     return False

#   i = 5
#   while i * i <= num:
#     if num % i == 0 or num % (i + 2) == 0:
#       return False
#     i += 6

#   return True

# # Example usage
# number = 12
# if is_prime(number):
#   print(f"{number} is a prime number.")
# else:
#   print(f"{number} is not a prime number.")


def fizzbuzz(start, end):
  """Prints numbers from start to end, replacing multiples of 3 with "Fizz",
  multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".

  Args:
      start (int): The starting number (inclusive).
      end (int): The ending number (inclusive).
  """

  for num in range(start, end + 1):
    if num % 15 == 0:  # Check for multiples of both 3 and 5 first (optimization)
      print("FizzBuzz")
    elif num % 3 == 0:
      print("Fizz")
    elif num % 5 == 0:
      print("Buzz")
    else:
      print(num)

# Example usage
fizzbuzz(1, 100)




