# StegaVault-CLI

## Folder Structure

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
│   ├── file_cli.py             # File encrypt/decrypt CLI
│   ├── image_cli.py            # Image steganography CLI
│   ├── audio_cli.py            # Audio steganography CLI
│   └── utils.py                # Common CLI helpers
│
├── main.py                     # Unified CLI entrypoint
├── requirements.txt
└── README.md
```
