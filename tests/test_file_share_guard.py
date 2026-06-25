import pytest
from file_share_guard import FileShareGuard

def test_create_share_without_password():
    guard = FileShareGuard()
    share_id = guard.create_share("test_file.txt")
    assert share_id in guard.shares
    assert guard.shares[share_id].password is None

def test_create_share_with_password():
    guard = FileShareGuard()
    share_id = guard.create_share("test_file.txt", "test_password")
    assert share_id in guard.shares
    assert guard.shares[share_id].password == "test_password"

def test_authenticate_without_password():
    guard = FileShareGuard()
    share_id = guard.create_share("test_file.txt")
    assert guard.authenticate(share_id, "")

def test_authenticate_with_password():
    guard = FileShareGuard()
    share_id = guard.create_share("test_file.txt", "test_password")
    assert guard.authenticate(share_id, "test_password")

def test_authenticate_with_wrong_password():
    guard = FileShareGuard()
    share_id = guard.create_share("test_file.txt", "test_password")
    assert not guard.authenticate(share_id, "wrong_password")

def test_get_file_name_with_password():
    guard = FileShareGuard()
    share_id = guard.create_share("test_file.txt", "test_password")
    assert guard.get_file_name(share_id, "test_password") == "test_file.txt"

def test_get_file_name_without_password():
    guard = FileShareGuard()
    share_id = guard.create_share("test_file.txt")
    assert guard.get_file_name(share_id, "") == "test_file.txt"

def test_get_file_name_with_wrong_password():
    guard = FileShareGuard()
    share_id = guard.create_share("test_file.txt", "test_password")
    assert guard.get_file_name(share_id, "wrong_password") is None
