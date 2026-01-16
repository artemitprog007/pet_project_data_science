import hashlib
import random

def generate_dsa_params():
    p = 23
    q = 11
    g = 4
    return p, q, g

def generate_dsa_keys(p, q, g):
    x = random.randint(1, q - 1)
    y = pow(g, x, p)
    return (x, (p, q, g, y))

def dsa_sign(message, private_key, params):
    x = private_key
    p, q, g = params
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q
    k = random.randint(1, q - 1)
    r = pow(g, k, p) % q
    k_inv = pow(k, q - 2, q)
    s = (k_inv * (h + x * r)) % q
    return (r, s)

def dsa_verify(message, signature, public_key):
    r, s = signature
    p, q, g, y = public_key
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q
    w = pow(s, q - 2, q)
    u1 = (h * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r

p, q, g = generate_dsa_params()
private_key, public_key = generate_dsa_keys(p, q, g)
message = "Digital Signature Test"

signature = dsa_sign(message, private_key, (p, q, g))
is_valid = dsa_verify(message, signature, public_key)

print(f"Parameters: p={p}, q={q}, g={g}")
print(f"Private Key (x): {private_key}")
print(f"Public Key (p, q, g, y): {public_key}")
print(f"Message: {message}")
print(f"Signature (r, s): {signature}")
print(f"Signature Valid: {is_valid}")
