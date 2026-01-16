import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1, temp2 = divmod(temp_phi, e)
        temp_phi, e = e, temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2, x1 = x1, x
        d, y1 = y1, y
    if temp_phi == 1:
        return d + phi

def generate_rsa_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    while gcd(e, phi) != 1:
        e += 2
    d = modinv(e, phi)
    return ((e, n), (d, n))

def rsa_encrypt(public_key, plaintext):
    e, n = public_key
    return pow(plaintext, e, n)

def rsa_decrypt(private_key, ciphertext):
    d, n = private_key
    return pow(ciphertext, d, n)

p = 61
q = 53
public_key, private_key = generate_rsa_keys(p, q)

message = 42
ciphertext = rsa_encrypt(public_key, message)
decrypted = rsa_decrypt(private_key, ciphertext)

print(f"p = {p}, q = {q}")
print(f"n = {public_key[1]}")
print(f"Public Key (e, n): {public_key}")
print(f"Private Key (d, n): {private_key}")
print(f"Message: {message}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted}")
