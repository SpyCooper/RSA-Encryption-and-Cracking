# Description: This program cracks a message that has been encrypted using RSA encryption

# import the sys module
import sys

# read in e and n on the first line
e, n = map(int, input().split())

# read in the rest of the text
m = sys.stdin.read()

# convert the message to a list of characters
message = list(m)

# find the value of d
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# calculate the value of phi
def find_prime_numbers_in_range(n):
    prime_numbers = []
    for i in range(2, n):
        if n % i == 0:
            prime_numbers.append(i)
            prime_numbers.append(n // i)
            break
    return prime_numbers

# find the prime numbers in the range of n
prime_numbers = find_prime_numbers_in_range(n)

# get the first 2 prime numbers
p = prime_numbers[0]
q = prime_numbers[1]

# calculate the value of phi
phi = (p - 1) * (q - 1)

# calculate the private key d
d = mod_inverse(e, phi)

# initialize the new string
character_string = ""
int_string = ""

# decrypt the message using RSA decryption
for i in range(len(message) - 1):
    c = (ord(message[i]) ** d) % n
    character_string += chr(c)
    int_string += str(c) + " "

# print the prime numbers
print(f"Prime numbers: {p}, {q}", file=sys.stderr)

# print the value of n
print(f"n: {n}", file=sys.stderr)

# print the private key to the standard error
print(f"Private key: {d}", file=sys.stderr)

# print the decrypted message as a list of integers to the standard error
print(f"Decrypted message in integers: \n{int_string}", file=sys.stderr)

# print the public key
print(f"Public key: {e}")

# print the decrypted message as a string
print(f"Unencrypted message: \n{character_string}")