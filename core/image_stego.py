from PIL import Image
import secrets
from cryptography.fernet import Fernet
from .crypto_utils import derive_key

MAGIC = b"STEG"


def _to_bits(data: bytes):
    for b in data:
        for i in range(7, -1, -1):
            yield (b >> i) & 1


def _from_bits(bits):
    out = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i : i + 8]:
            byte = (byte << 1) | b
        out.append(byte)
    return bytes(out)


def embed_message(img_path, message, password, out_path):
    img = Image.open(img_path).convert("RGB")
    pixels = list(img.getdata())

    salt = secrets.token_bytes(16)
    key = derive_key(password, salt)

    payload = MAGIC + salt + Fernet(key).encrypt(message.encode())
    bits = list(_to_bits(payload))

    if len(bits) > len(pixels) * 3:
        raise ValueError("Image too small")

    new_pixels = []
    bit_i = 0

    for r, g, b in pixels:
        if bit_i < len(bits):
            r = (r & ~1) | bits[bit_i]
            bit_i += 1
        if bit_i < len(bits):
            g = (g & ~1) | bits[bit_i]
            bit_i += 1
        if bit_i < len(bits):
            b = (b & ~1) | bits[bit_i]
            bit_i += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(out_path, "PNG")


def extract_message(img_path, password):
    img = Image.open(img_path).convert("RGB")
    bits = []

    for r, g, b in img.getdata():
        bits.extend([r & 1, g & 1, b & 1])

    data = _from_bits(bits)

    if not data.startswith(MAGIC):
        raise ValueError("No hidden data")

    salt = data[4:20]
    encrypted = data[20:]

    key = derive_key(password, salt)
    return Fernet(key).decrypt(encrypted).decode()
