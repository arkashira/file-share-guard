import hashlib
import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class Share:
    file_name: str
    password: Optional[str] = None

class FileShareGuard:
    def __init__(self):
        self.shares = {}

    def create_share(self, file_name: str, password: Optional[str] = None) -> str:
        share_id = hashlib.sha256(f"{file_name}{password}".encode()).hexdigest()
        self.shares[share_id] = Share(file_name, password)
        return share_id

    def authenticate(self, share_id: str, password: str) -> bool:
        if share_id not in self.shares:
            return False
        share = self.shares[share_id]
        if share.password is None:
            return True
        return hashlib.sha256(password.encode()).hexdigest() == hashlib.sha256(share.password.encode()).hexdigest()

    def get_file_name(self, share_id: str, password: str) -> Optional[str]:
        if self.authenticate(share_id, password):
            return self.shares[share_id].file_name
        return None
