# File Share Guard

A simple file share guard that allows you to create shares with optional password protection.

## Usage

1. Create a share with `FileShareGuard.create_share(file_name, password=None)`.
2. Authenticate with `FileShareGuard.authenticate(share_id, password)`.
3. Get the file name with `FileShareGuard.get_file_name(share_id, password)`.

## Testing

Run the tests with `python -m pytest`.
