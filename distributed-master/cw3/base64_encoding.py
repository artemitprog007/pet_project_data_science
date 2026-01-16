import base64

plaintext = b"Base64 Encoding Example"
encoded = base64.b64encode(plaintext)
decoded = base64.b64decode(encoded)

print(f"Plaintext: {plaintext}")
print(f"Base64 Encoded: {encoded}")
print(f"Decoded: {decoded}")

hex_encoded = plaintext.hex()
hex_decoded = bytes.fromhex(hex_encoded)
print(f"\nHex Encoded: {hex_encoded}")
print(f"Hex Decoded: {hex_decoded}")
