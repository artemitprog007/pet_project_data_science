import random

def diffie_hellman_exchange(p, g):
    a = random.randint(2, p - 2)
    b = random.randint(2, p - 2)
    A = pow(g, a, p)
    B = pow(g, b, p)
    shared_secret_alice = pow(B, a, p)
    shared_secret_bob = pow(A, b, p)
    return a, b, A, B, shared_secret_alice, shared_secret_bob

p = 23
g = 5

a, b, A, B, secret_alice, secret_bob = diffie_hellman_exchange(p, g)

print(f"Public parameters: p={p}, g={g}")
print(f"Alice's private key (a): {a}")
print(f"Alice's public key (A): {A}")
print(f"Bob's private key (b): {b}")
print(f"Bob's public key (B): {B}")
print(f"Alice's computed shared secret: {secret_alice}")
print(f"Bob's computed shared secret: {secret_bob}")
print(f"Secrets match: {secret_alice == secret_bob}")
