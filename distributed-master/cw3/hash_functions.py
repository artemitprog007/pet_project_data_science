import hashlib

message = b"Cryptography Hash Functions"

md5_hash = hashlib.md5(message).hexdigest()
sha1_hash = hashlib.sha1(message).hexdigest()
sha256_hash = hashlib.sha256(message).hexdigest()
sha512_hash = hashlib.sha512(message).hexdigest()
sha3_256_hash = hashlib.sha3_256(message).hexdigest()

print(f"Message: {message}")
print(f"MD5: {md5_hash}")
print(f"SHA-1: {sha1_hash}")
print(f"SHA-256: {sha256_hash}")
print(f"SHA-512: {sha512_hash}")
print(f"SHA3-256: {sha3_256_hash}")
