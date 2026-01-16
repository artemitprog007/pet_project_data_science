import hashlib
import hmac

secret_key = b"my_secret_key_12345"
message = b"Authenticate this message"

hmac_sha256 = hmac.new(secret_key, message, hashlib.sha256).hexdigest()
hmac_sha1 = hmac.new(secret_key, message, hashlib.sha1).hexdigest()
hmac_sha512 = hmac.new(secret_key, message, hashlib.sha512).hexdigest()

print(f"Secret Key: {secret_key}")
print(f"Message: {message}")
print(f"HMAC-SHA256: {hmac_sha256}")
print(f"HMAC-SHA1: {hmac_sha1}")
print(f"HMAC-SHA512: {hmac_sha512}")

def verify_hmac(key, msg, expected_hmac, hash_algo):
    computed_hmac = hmac.new(key, msg, hash_algo).hexdigest()
    return hmac.compare_digest(computed_hmac, expected_hmac)

is_valid = verify_hmac(secret_key, message, hmac_sha256, hashlib.sha256)
print(f"\nHMAC Verification: {is_valid}")
