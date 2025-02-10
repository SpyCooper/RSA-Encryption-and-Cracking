# RSA Encryption and Cracking

Two program that does RSA encryption and then cracks the RSA encryption that was made for my cyber security class.

Both files will read the `e` and `n` values and then the text that is being encrypted from the standard input. Both programs will output the public key and the encrypted/decrypted text to the standard output. Other info about the program (prime numbers, private key, n value, phi of n, encoded text as integers, etc.) are printed to the standard error.

The `n` value is a public key that contains at least two prime numbers that multiply to it and that has to be below 1114111. This restriction is due to the highest value that can be held in a unicode value, since the encrypted data is held in unicode. Ex: n = 77, 7 * 11 = 77

The `e` value has to be a value that is 1 < e < λ(n). λ(n) is  (p - 1)(q - 1) where p and q are two prime numbers that multiply together to get `n`.


## Explanation of RSA encryption

1. The program reads in a `e`, `n`, and text to be encrypted from the standard input

2. The the first two prime numbers that multiply to the n value to use as the p and q values.

3. Find the λ(n) value
    - λ(n) = (p - 1)(q - 1)

4. Find `d` with the reverse mod of e and λ(n) to be saved for the private key when decrypting is necessary

5. Take the original message (c) and encrypt it
    - (c ^ e) % n 

## Explanation of RSA Cracking

1. The program reads in a `e`, `n`, and text to be encrypted from the standard input

2. The the first two prime numbers that multiply to the n value to use as the p and q values.

3. Find the λ(n) value
    - λ(n) = (p - 1)(q - 1)

4. Find `d` with the reverse mod of e and λ(n)

5. Decrypt using the original message (c)
    - ( c ^ d ) % n

## Running

I ran this in python3 using the following command formats:

```python3 rsa_encyption.py < tests/encryption_test_1.input > tests/encryption_test_1.output  2> tests/encryption_test_1_log.txt```

```python3 rsa_cracking.py < tests/decryption_test_1.input > tests/decryption_test_1.output 2> tests/decryption__test_1_log.txt```