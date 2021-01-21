import os
import paramiko

# Generate new key and write private key to file
key1 = paramiko.RSAKey.generate(1024)
print(key1.get_base64())
with open('id_rsa', 'w') as f_out:
    key1.write_private_key(f_out)

# Fix private key permission
os.chmod('id_rsa', 0o0600)

# Read written private key and show public key
key2 = paramiko.RSAKey.from_private_key_file('id_rsa')
print(key2.get_base64())