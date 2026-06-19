import pytest
from file_share_guard import FileMetadata, upload_file, download_file, get_encryption_key
import os

def test_upload_file():
    file_data = b'Hello, World!'
    filename = 'example.txt'
    metadata = upload_file(file_data, filename)
    assert metadata.filename == filename
    assert metadata.encryption_key
    os.remove(f'{filename}.enc')
    os.remove(f'{filename}.meta')

def test_download_file():
    file_data = b'Hello, World!'
    filename = 'example.txt'
    upload_file(file_data, filename)
    downloaded_data = download_file(filename)
    assert downloaded_data == file_data
    os.remove(f'{filename}.enc')
    os.remove(f'{filename}.meta')

def test_get_encryption_key():
    file_data = b'Hello, World!'
    filename = 'example.txt'
    metadata = upload_file(file_data, filename)
    encryption_key = get_encryption_key(filename)
    assert encryption_key == metadata.encryption_key
    os.remove(f'{filename}.enc')
    os.remove(f'{filename}.meta')

def test_upload_file_edge_case():
    file_data = b''
    filename = 'example.txt'
    metadata = upload_file(file_data, filename)
    assert metadata.filename == filename
    assert metadata.encryption_key
    os.remove(f'{filename}.enc')
    os.remove(f'{filename}.meta')

def test_download_file_edge_case():
    filename = 'non_existent_file.txt'
    downloaded_data = download_file(filename)
    assert downloaded_data is None
