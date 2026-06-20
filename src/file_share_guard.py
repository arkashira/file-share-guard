import argparse
import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class FileShareGuard:
    encryption_key: str

    def encrypt_file(self, file_data: str) -> str:
        encrypted_data = ""
        for i, char in enumerate(file_data):
            encrypted_data += chr((ord(char) + ord(self.encryption_key[i % len(self.encryption_key)])) % 256)
        return encrypted_data

    def decrypt_file(self, encrypted_data: str) -> str:
        decrypted_data = ""
        for i, char in enumerate(encrypted_data):
            decrypted_data += chr((ord(char) - ord(self.encryption_key[i % len(self.encryption_key)])) % 256)
        return decrypted_data

    def manage_encryption_keys(self, new_key: Optional[str] = None) -> str:
        if new_key:
            self.encryption_key = new_key
        return self.encryption_key

def main():
    parser = argparse.ArgumentParser(description="File Share Guard")
    parser.add_argument("--encrypt", help="Encrypt a file")
    parser.add_argument("--decrypt", help="Decrypt a file")
    parser.add_argument("--key", help="Set a new encryption key")
    args = parser.parse_args()

    file_share_guard = FileShareGuard("default_key")

    if args.encrypt:
        encrypted_data = file_share_guard.encrypt_file(args.encrypt)
        print(encrypted_data)

    elif args.decrypt:
        decrypted_data = file_share_guard.decrypt_file(args.decrypt)
        print(decrypted_data)

    elif args.key:
        new_key = file_share_guard.manage_encryption_keys(args.key)
        print(new_key)

if __name__ == "__main__":
    main()
