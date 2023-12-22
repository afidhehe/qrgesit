from base64 import b64encode
from io import BytesIO

import qrcode


def get_qr_code(data: str, box_size=6, border=4) -> str:
    qr_code_bytes = get_qr_code_bytes(data, format="PNG", box_size=box_size, border=border)
    base_64_string = bytes_to_base64_string(qr_code_bytes)

    return add_file_info(base_64_string)


def add_file_info(data: str) -> str:
    """Add info about the file type and encoding.

    This is required so the browser can make sense of the data."""
    return f"data:image/png;base64, {data}"


def get_qr_code_bytes(data, format: str, box_size=6, border=4) -> bytes:
    """Create a QR code and return the bytes."""
    img = qrcode.make(data, box_size=box_size, border=border)

    buffered = BytesIO()
    img.save(buffered, format=format)

    return buffered.getvalue()


def bytes_to_base64_string(data: bytes) -> str:
    """Convert bytes to a base64 encoded string."""
    return b64encode(data).decode("utf-8")