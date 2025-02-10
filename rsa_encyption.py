# Description: This program encrypts a message using RSA encryption

# import the sys module
import sys

# find the prime numbers in the range of n and that multiply to n
def find_prime_numbers_in_range(n):
    prime_numbers = []
    for i in range(2, n):
        if n % i == 0:
            prime_numbers.append(i)
            if len(prime_numbers) == 2:
                if prime_numbers[0] * prime_numbers[1] == n:
                    break
                else:
                    prime_numbers.pop()
    if len(prime_numbers) < 2 or prime_numbers[0] * prime_numbers[1] != n:
        raise ValueError("Cannot find two prime numbers that multiply to n")
    return prime_numbers

# read in e and n on the first line
e, n = map(int, input().split())

# check if the value of n is greater than 1114111 (the maximum value of a unicode character)
if n > 1114111:
    raise ValueError("n must be less than or equal to 1,114,111")

# read in the rest of the text
m = sys.stdin.read()

# convert the message to a list of characters
message = list(m)

# find the prime numbers in the range of n
prime_numbers = find_prime_numbers_in_range(n)

# get the first 2 prime numbers
p = prime_numbers[0]
q = prime_numbers[1]

# calculate the value of phi
phi = (p - 1) * (q - 1)

# initialize the new string
character_string = ""
int_string = ""

# encrypt the message using RSA encryption
for i in range(len(message)):
    c = (ord(message[i]) ** e) % n
    character_string += chr(c)
    int_string += str(c) + " "

# find the value of d
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# calculate the private key d
d = mod_inverse(e, phi)

# print the prime numbers to the standard error
print(f"Prime numbers: {p}, {q}", file=sys.stderr)

# print the value of n to the standard error
print(f"n: {n}", file=sys.stderr)

# print the value of phi to the standard error
print(f"Phi of n: {phi}", file=sys.stderr)

# print the private key to the standard error
print(f"Private key: {d}", file=sys.stderr)

# print the original message in ascii code to the standard error
print(f"Message in ASCII: {list(map(ord, message))}", file=sys.stderr)

# print the encrypted message as a list of numbers to the standard error
print(f"Message encoded: {int_string.strip()}", file=sys.stderr)

# print the public key to the standard error
print(f"Public key: {e}")

# print the encrypted message to the standard output
print(character_string.strip())
