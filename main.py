import argparse
from cli.file_cli import handle_file
from cli.image_cli import handle_image
from cli.audio_cli import handle_audio


def main():
    parser = argparse.ArgumentParser(
        prog="stegavault",
        description=(
            "StegaVault CLI 🔐\n\n"
            "A beginner-friendly encryption & steganography toolkit.\n"
            "Supports:\n"
            "  • File encryption/decryption\n"
            "  • Image steganography (PNG)\n"
            "  • Audio steganography (WAV)\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    subparsers = parser.add_subparsers(
        title="Available modules",
        dest="module",
        required=True,
    )

    # -------- FILE -------- #
    file_parser = subparsers.add_parser(
        "file",
        help="Encrypt or decrypt files",
    )
    file_parser.add_argument(
        "-i", "--input",
        required=True,
        help="Input file path (any file type)",
    )
    file_parser.add_argument(
        "-o", "--output",
        help="Output file path (optional)",
    )
    file_parser.add_argument(
        "-p", "--password",
        required=True,
        help="Password for encryption/decryption",
    )

    mode = file_parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "-e", "--encrypt",
        action="store_true",
        help="Encrypt the input file",
    )
    mode.add_argument(
        "-d", "--decrypt",
        action="store_true",
        help="Decrypt the encrypted file",
    )

    file_parser.set_defaults(func=handle_file)

    # -------- IMAGE -------- #
    image_parser = subparsers.add_parser(
        "image",
        help="Image steganography (PNG)",
    )
    image_parser.add_argument(
        "-i", "--image",
        required=True,
        help="Carrier image path (PNG recommended)",
    )
    image_parser.add_argument(
        "-m", "--message",
        help="Secret message to hide (for encryption)",
    )
    image_parser.add_argument(
        "-o", "--output",
        help="Output image name (default: stego.png)",
    )
    image_parser.add_argument(
        "-p", "--password",
        required=True,
        help="Password for encryption/decryption",
    )

    mode = image_parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "-e", "--embed",
        action="store_true",
        help="Encrypt & embed message into image",
    )
    mode.add_argument(
        "-x", "--extract",
        action="store_true",
        help="Extract & decrypt hidden message",
    )

    image_parser.set_defaults(func=handle_image)

    # -------- AUDIO -------- #
    audio_parser = subparsers.add_parser(
        "audio",
        help="Audio steganography (WAV)",
    )
    audio_parser.add_argument(
        "-i", "--audio",
        required=True,
        help="Carrier WAV file (16-bit PCM)",
    )
    audio_parser.add_argument(
        "-m", "--message",
        help="Secret message to hide (for encryption)",
    )
    audio_parser.add_argument(
        "-o", "--output",
        help="Output WAV file (default: stego.wav)",
    )
    audio_parser.add_argument(
        "-p", "--password",
        required=True,
        help="Password for encryption/decryption",
    )

    mode = audio_parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "-e", "--embed",
        action="store_true",
        help="Encrypt & embed message into audio",
    )
    mode.add_argument(
        "-x", "--extract",
        action="store_true",
        help="Extract & decrypt hidden message",
    )

    audio_parser.set_defaults(func=handle_audio)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
