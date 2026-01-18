from core.file_crypto import encrypt_file, decrypt_file


def handle_file(args):
    if args.encrypt:
        encrypt_file(args.input, args.password)
        print("[+] File encrypted successfully")

    elif args.decrypt:
        decrypt_file(args.input, args.password)
        print("[+] File decrypted successfully")
