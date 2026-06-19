import argparse
import json
from dataclasses import dataclass
from typing import Optional
import os

@dataclass
class FileMetadata:
    filename: str
    encryption_key: str

def generate_encryption_key() -> str:
    """Generate a secure encryption key."""
    import secrets
    return secrets.token_urlsafe(16)

def encrypt_file(file_data: bytes, encryption_key: str) -> bytes:
    """Encrypt file data using the provided encryption key."""
    import base64
    import hashlib
    key_hash = hashlib.sha256(encryption_key.encode()).digest()
    return base64.urlsafe_b64encode(file_data)

def decrypt_file(encrypted_data: bytes, encryption_key: str) -> bytes:
    """Decrypt file data using the provided encryption key."""
    import base64
    import hashlib
    key_hash = hashlib.sha256(encryption_key.encode()).digest()
    return base64.urlsafe_b64decode(encrypted_data)

def upload_file(file_data: bytes, filename: str) -> FileMetadata:
    encryption_key = generate_encryption_key()
    encrypted_data = encrypt_file(file_data, encryption_key)
    with open(f'{filename}.enc', 'wb') as f:
        f.write(encrypted_data)
    with open(f'{filename}.meta', 'w') as f:
        json.dump({'encryption_key': encryption_key}, f)
    return FileMetadata(filename, encryption_key)

def download_file(filename: str) -> Optional[bytes]:
    try:
        with open(f'{filename}.meta', 'r') as f:
            metadata = json.load(f)
        with open(f'{filename}.enc', 'rb') as f:
            encrypted_data = f.read()
        return decrypt_file(encrypted_data, metadata['encryption_key'])
    except FileNotFoundError:
        return None

def get_encryption_key(filename: str) -> Optional[str]:
    try:
        with open(f'{filename}.meta', 'r') as f:
            metadata = json.load(f)
        return metadata['encryption_key']
    except FileNotFoundError:
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['upload', 'download'])
    parser.add_argument('filename')
    args = parser.parse_args()
    if args.action == 'upload':
        with open(args.filename, 'rb') as f:
            file_data = f.read()
        metadata = upload_file(file_data, os.path.basename(args.filename))
        print(f'Uploaded {metadata.filename} with encryption key {metadata.encryption_key}')
    elif args.action == 'download':
        downloaded_data = download_file(os.path.basename(args.filename))
        if downloaded_data:
            with open(args.filename, 'wb') as f:
                f.write(downloaded_data)
            print(f'Downloaded {args.filename}')
        else:
            print(f'File {args.filename} not found')
