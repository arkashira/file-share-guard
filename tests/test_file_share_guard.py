import datetime
from file_share_guard import FileShareGuard

def test_set_expiration_date():
    guard = FileShareGuard()
    guard.set_expiration_date("test_file", datetime.date.today() + datetime.timedelta(days=1))
    assert guard.get_expiration_date("test_file") == datetime.date.today() + datetime.timedelta(days=1)

def test_is_expired():
    guard = FileShareGuard()
    guard.set_expiration_date("test_file", datetime.date.today() - datetime.timedelta(days=1))
    assert guard.is_expired("test_file")

def test_notify_expiration():
    guard = FileShareGuard()
    guard.set_expiration_date("test_file", datetime.date.today() + datetime.timedelta(days=1))
    guard.notify_expiration("test_file")

def test_expire_file_share():
    guard = FileShareGuard()
    guard.set_expiration_date("test_file", datetime.date.today() - datetime.timedelta(days=1))
    guard.expire_file_share("test_file")
    assert "test_file" not in guard.file_shares

def test_get_expiration_date_non_existent_file():
    guard = FileShareGuard()
    assert guard.get_expiration_date("non_existent_file") is None
