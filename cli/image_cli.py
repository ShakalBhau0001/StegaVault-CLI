from core.image_stego import embed_message, extract_message


def handle_image(args):
    if args.embed:
        if not args.message:
            raise ValueError("Message is required for embedding")

        output = args.output or "stego.png"
        embed_message(
            args.image,
            args.message,
            args.password,
            output,
        )
        print(f"[+] Message embedded → {output}")

    elif args.extract:
        msg = extract_message(args.image, args.password)
        print("[+] Extracted message:")
        print(msg)
