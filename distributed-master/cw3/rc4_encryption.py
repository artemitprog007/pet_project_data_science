import os

def rc4_ksa(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def rc4_prga(S, data):
    i = j = 0
    result = bytearray()
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        result.append(byte ^ K)
    return bytes(result)

def rc4_encrypt(key, plaintext):
    S = rc4_ksa(key)
    return rc4_prga(S, plaintext)

def rc4_decrypt(key, ciphertext):
    S = rc4_ksa(key)
    return rc4_prga(S, ciphertext)

rc4_key = os.urandom(16)
plaintext = b"RC4 Stream Cipher Test"

ciphertext = rc4_encrypt(rc4_key, plaintext)
decrypted = rc4_decrypt(rc4_key, ciphertext)

print(f"Key: {rc4_key.hex()}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Decrypted: {decrypted}")
