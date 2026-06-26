import pytest
from file_share_guard import FileShareLink, generate_link, upload_file, view_link, copy_link

def test_generate_link():
    link = generate_link("test_file.txt", "1h")
    assert link.file_name == "test_file.txt"
    assert link.link.startswith("test_file.txt_")
    assert link.expiration_time == "1h"

def test_generate_link_with_password():
    link = generate_link("test_file.txt", "1h", "password123")
    assert link.file_name == "test_file.txt"
    assert link.link.startswith("test_file.txt_")
    assert link.expiration_time == "1h"
    assert link.password == "password123"

def test_upload_file():
    link = upload_file("test_file.txt", "1h")
    assert link.file_name == "test_file.txt"
    assert link.link.startswith("test_file.txt_")
    assert link.expiration_time == "1h"

def test_view_link():
    link = FileShareLink("test_file.txt", "test_link", "1h")
    assert view_link(link) == "test_link"

def test_copy_link():
    link = "test_link"
    assert copy_link(link) == "test_link"

def test_generate_link_invalid_expiration_time():
    with pytest.raises(ValueError):
        generate_link("test_file.txt", "invalid_time")

def test_upload_file_invalid_expiration_time():
    with pytest.raises(ValueError):
        upload_file("test_file.txt", "invalid_time")
