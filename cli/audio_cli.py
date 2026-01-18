from core.audio_stego import embed_audio, extract_audio


def handle_audio(args):
    if args.embed:
        if not args.message:
            raise ValueError("Message is required for embedding")

        output = args.output or "stego.wav"
        embed_audio(
            args.audio,
            args.message,
            args.password,
            output,
        )
        print(f"[+] Message embedded → {output}")

    elif args.extract:
        msg = extract_audio(args.audio, args.password)
        print("[+] Extracted message:")
        print(msg)
