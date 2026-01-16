import os

def des_encrypt_simple(key, plaintext):
    result = bytearray()
    for i, byte in enumerate(plaintext):
        result.append(byte ^ key[i % len(key)])
    return bytes(result)

def des_decrypt_simple(key, ciphertext):
    return des_encrypt_simple(key, ciphertext)

des_key = os.urandom(8)
plaintext = b"Security"
ciphertext = des_encrypt_simple(des_key, plaintext)
decrypted = des_decrypt_simple(des_key, ciphertext)

print(f"Key: {des_key.hex()}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Decrypted: {decrypted}")
