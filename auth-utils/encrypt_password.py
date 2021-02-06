from passlib.hash import sha512_crypt

# Encrypt password "securePassword"
pw_string = "securePassword"
pw_hash = sha512_crypt.hash("securePassword")

# Verify password encryption
if sha512_crypt.verify(pw_string, pw_hash):
    print(f"Encrypted shadow is: {pw_hash}")