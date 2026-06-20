from file_share_guard import FileShareGuard

def test_encrypt_file():
    file_share_guard = FileShareGuard("test_key")
    file_data = "Hello, World!"
    encrypted_data = file_share_guard.encrypt_file(file_data)
    assert encrypted_data != file_data

def test_decrypt_file():
    file_share_guard = FileShareGuard("test_key")
    file_data = "Hello, World!"
    encrypted_data = file_share_guard.encrypt_file(file_data)
    decrypted_data = file_share_guard.decrypt_file(encrypted_data)
    assert decrypted_data == file_data

def test_manage_encryption_keys():
    file_share_guard = FileShareGuard("test_key")
    new_key = "new_test_key"
    updated_key = file_share_guard.manage_encryption_keys(new_key)
    assert updated_key == new_key

def test_encrypt_file_edge_case():
    file_share_guard = FileShareGuard("test_key")
    file_data = ""
    encrypted_data = file_share_guard.encrypt_file(file_data)
    assert encrypted_data == ""

def test_decrypt_file_edge_case():
    file_share_guard = FileShareGuard("test_key")
    encrypted_data = ""
    decrypted_data = file_share_guard.decrypt_file(encrypted_data)
    assert decrypted_data == ""
