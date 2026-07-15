import hashlib


def calculate_sha256(file_bytes: bytes) -> str:
    sha = hashlib.sha256()
    sha.update(file_bytes)
    return sha.hexdigest()
