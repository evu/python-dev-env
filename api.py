"""ROT13 Encoder / Decoder API."""
import logging
import os

import hug


ALPHABET = "abcdefghijklmnopqrstuvwxyz"


# Grab app-level logger
app_logger = logging.getLogger("hugapp")

# Consolidate logging
gunicorn_logger = logging.getLogger("gunicorn.error")
app_logger.handlers = gunicorn_logger.handlers
app_logger.setLevel(gunicorn_logger.level)


@hug.get("/encode", versions=1, examples="text=evu")
def encode_handler_v1(text):
    """Route handler for v1/encode route."""
    return {"data": rot13(text)}


@hug.get("/encode", versions=2, examples="text=evu")
def encode_handler_v2(text):
    """Route handler for v2/encode route."""
    return {"result": rot13(text)}


def rot13(text):
    """Return an alpha string with each character rotated by 13 places in the alphabet."""
    app_name = os.getenv("APPLICATION_NAME", default="unknown")

    app_logger.info("HELLLLOOOOOOO")

    app_logger.info("[%s] Request to encode text :'%s'", app_name, text)

    encoded = []

    for char in text.lower():
        if char in ALPHABET:
            encoded.append(
                ALPHABET[(ALPHABET.index(char) + 13) % len(ALPHABET)]
            )

    return "".join(encoded)
