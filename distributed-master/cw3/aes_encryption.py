import os

def aes_encrypt_simple(key, plaintext):
    block_size = 16
    padded = plaintext + b'\x00' * (block_size - len(plaintext) % block_size)
    result = bytearray()
    for i, byte in enumerate(padded):
        result.append(byte ^ key[i % len(key)])
    return bytes(result)

def aes_decrypt_simple(key, ciphertext):
    decrypted = bytearray()
    for i, byte in enumerate(ciphertext):
        decrypted.append(byte ^ key[i % len(key)])
    return bytes(decrypted).rstrip(b'\x00')

aes_key_128 = os.urandom(16)
aes_key_256 = os.urandom(32)
plaintext = b"Advanced Encryption Standard"

ciphertext_128 = aes_encrypt_simple(aes_key_128, plaintext)
decrypted_128 = aes_decrypt_simple(aes_key_128, ciphertext_128)

ciphertext_256 = aes_encrypt_simple(aes_key_256, plaintext)
decrypted_256 = aes_decrypt_simple(aes_key_256, ciphertext_256)

print("AES-128:")
print(f"Key: {aes_key_128.hex()}")
print(f"Ciphertext: {ciphertext_128.hex()}")
print(f"Decrypted: {decrypted_128}")
print()
print("AES-256:")
print(f"Key: {aes_key_256.hex()}")
print(f"Ciphertext: {ciphertext_256.hex()}")
print(f"Decrypted: {decrypted_256}")
