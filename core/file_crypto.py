import os
import secrets
from cryptography.fernet import Fernet
from .crypto_utils import derive_key


MAGIC = b"FILE"


def encrypt_file(path: str, password: str) -> str:
    with open(path, "rb") as f:
        data = f.read()

    salt = secrets.token_bytes(16)
    key = derive_key(password, salt)
    encrypted = Fernet(key).encrypt(data)

    name = os.path.basename(path).encode()
    out = path + ".enc"

    with open(out, "wb") as f:
        f.write(MAGIC)
        f.write(salt)
        f.write(len(name).to_bytes(2, "big"))
        f.write(name)
        f.write(encrypted)

    return out


def decrypt_file(path: str, password: str) -> str:
    with open(path, "rb") as f:
        if f.read(4) != MAGIC:
            raise ValueError("Invalid encrypted file")

        salt = f.read(16)
        name_len = int.from_bytes(f.read(2), "big")
        name = f.read(name_len).decode()
        encrypted = f.read()

    key = derive_key(password, salt)
    decrypted = Fernet(key).decrypt(encrypted)

    out = os.path.join(os.path.dirname(path), name)
    with open(out, "wb") as f:
        f.write(decrypted)

    return out
