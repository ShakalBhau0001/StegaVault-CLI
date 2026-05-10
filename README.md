# 🗝️ StegaVault-CLI

### Unified Encryption & Steganography Toolkit (Command‑Line Edition)

**StegaVault‑CLI** is a powerful, password‑based **encryption and steganography command‑line tool** built entirely in **Python (3.12.x compatible)**.
It is designed for **developers, security learners, and power users** who prefer terminal‑based workflows and scripting.
Using simple and consistent CLI commands, users can:
  - Encrypt & decrypt files
  - Hide encrypted messages inside images
  - Hide encrypted messages inside audio files

All operations are performed **locally**, with **zero network usage**, ensuring full privacy and offline security.

---

## 🖥️ Looking for a GUI Version?

If you prefer a clean, beginner-friendly graphical interface instead of terminal commands:

👉 **StegaVault-GUI** provides the same core features with a modern desktop UI built using CustomTkinter.

> 🔗 GUI Repository: **[StegaVault-GUI](https://github.com/ShakalBhau0001/StegaVault-GUI)**

---

## ✨ Key Philosophy

StegaVault‑CLI follows three strict principles:

1. **Security‑first** – modern cryptography only, no shortcuts
2. **CLI‑friendly** – clean flags, predictable commands
3. **Modular architecture** – core logic isolated from CLI layer

This is **not a demo or toy project**. Each module is independently usable and follows consistent cryptographic rules.

---

## 🧩 Included Modules

### 🔐 File Encryption

Encrypt or decrypt *any* file using a password.

**Features**

* Supports all file types
* Encrypted output: `.enc`
* Original filename restored on decryption
* Password‑based key derivation (PBKDF2)

**Use‑case**

> Secure documents, backups, archives, binaries

---

### 🖼️ Image Steganography (PNG)

Hide encrypted text inside PNG images using **LSB steganography**.

**Features**

* Password‑protected payload
* MAGIC header integrity validation
* Lossless PNG output enforced
* Detects wrong password or corrupted images

**Use‑case**

> Invisible message transfer, steganography research

---

### 🔊 Audio Steganography (WAV)

Hide encrypted text inside **16‑bit PCM WAV** audio files.

**Features**

* Works only with uncompressed WAV
* Password‑based encryption
* Payload integrity validation
* Clean extraction with strong error handling

**Use‑case**
> Audio‑based covert communication experiments

---

## 📁 Project Structure

```bash
StegaVault-CLI/
│
├── core/
│   ├── __init__.py
│   ├── crypto_utils.py
│   ├── file_crypto.py
│   ├── image_stego.py
│   └── audio_stego.py
│
├── cli/
│   ├── __init__.py
│   ├── file_cli.py
│   ├── image_cli.py
│   ├── audio_cli.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

> ✔ Core logic and CLI interface are **strictly separated** for maintainability and extensibility.

---

## 🧪 Cryptography Details

| Component      | Implementation          |
| -------------- | ----------------------- |
| Encryption     | Fernet (AES‑128 + HMAC) |
| Key Derivation | PBKDF2‑HMAC‑SHA256      |
| Iterations     | 390,000                 |
| Salt           | Random per operation    |
| Integrity      | MAGIC header validation |

> ⚠️ Lossy formats (JPEG, MP3) are intentionally avoided for output to prevent data corruption.

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/ShakalBhau0001/StegaVault-CLI.git
cd StegaVault-CLI
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Help Command

```bash
python main.py --help
```

This will display all available modules and usage instructions.

---

## 🧪 CLI Usage Examples

> **Syntax**
> python main.py <module> [options]

Modules:

* `file`   → File encryption / decryption
* `image`  → Image steganography (PNG)
* `audio`  → Audio steganography (WAV)

---

## 📁 File Encryption

### 🔐 ENCODE / ENCRYPT FILE

**Encrypt (short flags)**

```bash
python main.py file -i secret.pdf -p mypass123 -e
```

**Encrypt (long flags)**

```bash
python main.py file --input secret.pdf --password mypass123 --encrypt
```

---

### 🔓 DECODE / DECRYPT FILE

**Decrypt (short flags)**

```bash
python main.py file -i secret.pdf.enc -p mypass123 -d
```

**Decrypt (long flags)**

```bash
python main.py file --input secret.pdf.enc --password mypass123 --decrypt
```

---

## 🖼️ Image Steganography (PNG)

### 🧬 ENCODE / EMBED MESSAGE

**Embed (short flags)**

```bash
python main.py image -i cover.png -m "Hello Stego" -p 1234 -e
```

**Embed (long flags)**

```bash
python main.py image --image cover.png --message "Hello Stego" --password 1234 --embed
```

---

### 📤 DECODE / EXTRACT MESSAGE

**Extract (short flags)**

```bash
python main.py image -i stego.png -p 1234 -x
```

**Extract (long flags)**

```bash
python main.py image --image stego.png --password 1234 --extract
```

---

## 🔊 Audio Steganography (WAV)

### 🧬 ENCODE / EMBED MESSAGE

**Embed (short flags)**

```bash
python main.py audio -i clean.wav -m "Hello Audio" -p 12345 -e
```

**Embed (long flags)**

```bash
python main.py audio --audio clean.wav --message "Hello Audio" --password 12345 --embed
```

---

### 📤 DECODE / EXTRACT MESSAGE

**Extract (short flags)**

```bash
python main.py audio -i stego.wav -p 12345 -x
```

**Extract (long flags)**

```bash
python main.py audio --audio stego.wav --password 12345 --extract
```

---

## 🆘 Help Commands

**Global help**

```bash
python main.py --help
```

**Module help**

```bash
python main.py file --help
python main.py image --help
python main.py audio --help
```

---

## ⚠️ Important Notes

- `file`, `image`, `audio` are **modules**, not flags
- Module name must come **immediately after** `main.py`
- Flags are **case-sensitive**
- Short and long flags both work
- Encode = input → output
- Decode = stego/encrypted file → original data

---

## 📦 requirements.txt

```txt
cryptography
pillow
```

_No unnecessary or hidden dependencies_

---

## ⚠️ Security Disclaimer

This project is intended for **educational and research purposes**.
Although it uses modern cryptographic primitives, it has **not undergone formal security audits**.
Do **not** use it for protecting high‑value or life‑critical data.

---

## 🛣️ Roadmap

- Shell auto‑completion support
- Batch processing mode
- Linux & macOS packaging
- PyInstaller standalone binaries

---

## 🪪 Author

> Developer: **Shakal Bhau**

> GitHub: **[ShakalBhau0001](https://github.com/ShakalBhau0001)**

---

> “Strong security doesn’t need a GUI — it needs discipline.”

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---
