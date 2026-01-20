import wave
import struct
import secrets
from cryptography.fernet import Fernet
from .crypto_utils import derive_key

MAGIC = b"AUDS"


def embed_audio(wav_path, message: bytes, password: str, out_path):
    with wave.open(wav_path, "rb") as w:
        params = w.getparams()
        frames = bytearray(w.readframes(w.getnframes()))

    salt = secrets.token_bytes(16)
    key = derive_key(password, salt)

    encrypted = Fernet(key).encrypt(message)

    payload = MAGIC + salt + struct.pack(">I", len(encrypted)) + encrypted

    bits = [(byte >> i) & 1 for byte in payload for i in range(7, -1, -1)]

    if len(bits) > len(frames):
        raise ValueError("Audio file too small for message")

    for i, bit in enumerate(bits):
        frames[i] = (frames[i] & ~1) | bit

    with wave.open(out_path, "wb") as w:
        w.setparams(params)
        w.writeframes(frames)


def extract_audio(wav_path, password):
    with wave.open(wav_path, "rb") as w:
        frames = bytearray(w.readframes(w.getnframes()))

    bits = [b & 1 for b in frames]

    # Read first 24 bytes
    header_bits = bits[: 24 * 8]
    header = _bits_to_bytes(header_bits)

    if not header.startswith(MAGIC):
        raise ValueError("No hidden audio data found")

    salt = header[4:20]
    size = struct.unpack(">I", header[20:24])[0]

    payload_bits = bits[: (24 + size) * 8]
    payload = _bits_to_bytes(payload_bits)

    encrypted = payload[24:]

    key = derive_key(password, salt)
    return Fernet(key).decrypt(encrypted).decode()


def _bits_to_bytes(bits):
    out = bytearray()
    for i in range(0, len(bits), 8):
        b = 0
        for bit in bits[i : i + 8]:
            b = (b << 1) | bit
        out.append(b)
    return bytes(out)
