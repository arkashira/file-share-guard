import argparse
import dataclasses
import json
import os
from datetime import datetime, timedelta

@dataclasses.dataclass
class FileShareLink:
    file_name: str
    link: str
    expiration_time: str
    password: str = None

def parse_expiration_time(expiration_time: str) -> timedelta:
    """Parse expiration time string into a timedelta object."""
    if expiration_time.endswith('s'):
        return timedelta(seconds=int(expiration_time[:-1]))
    elif expiration_time.endswith('m'):
        return timedelta(minutes=int(expiration_time[:-1]))
    elif expiration_time.endswith('h'):
        return timedelta(hours=int(expiration_time[:-1]))
    elif expiration_time.endswith('d'):
        return timedelta(days=int(expiration_time[:-1]))
    else:
        raise ValueError("Invalid expiration time format")

def generate_link(file_name: str, expiration_time: str, password: str = None) -> FileShareLink:
    """Generate a link with optional password protection and expiration time."""
    try:
        parse_expiration_time(expiration_time)
    except ValueError:
        raise ValueError("Invalid expiration time format")
    
    link = f"{file_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    if password:
        link += f"?password={password}"
    return FileShareLink(file_name, link, expiration_time, password)

def upload_file(file_path: str, expiration_time: str, password: str = None) -> FileShareLink:
    """Upload a file and generate a link."""
    file_name = os.path.basename(file_path)
    return generate_link(file_name, expiration_time, password)

def view_link(link: FileShareLink) -> str:
    """View and return the generated link."""
    return link.link

def copy_link(link: str) -> str:
    """Copy and return the generated link."""
    return link
