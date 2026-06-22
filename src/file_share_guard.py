import datetime
import json
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class FileShare:
    file_name: str
    expiration_date: datetime.date

class FileShareGuard:
    def __init__(self):
        self.file_shares: Dict[str, FileShare] = {}

    def set_expiration_date(self, file_name: str, expiration_date: datetime.date):
        self.file_shares[file_name] = FileShare(file_name, expiration_date)

    def get_expiration_date(self, file_name: str) -> Optional[datetime.date]:
        file_share = self.file_shares.get(file_name)
        if file_share is None:
            return None
        return file_share.expiration_date

    def is_expired(self, file_name: str) -> bool:
        if file_name not in self.file_shares:
            return True
        return self.file_shares[file_name].expiration_date < datetime.date.today()

    def notify_expiration(self, file_name: str):
        if file_name in self.file_shares:
            if self.file_shares[file_name].expiration_date - datetime.date.today() == datetime.timedelta(days=1):
                print(f"File share {file_name} is about to expire")

    def expire_file_share(self, file_name: str):
        if self.is_expired(file_name):
            if file_name in self.file_shares:
                del self.file_shares[file_name]
                print(f"File share {file_name} has expired and been removed")
