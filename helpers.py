import os

def save_secret_to_file(path, data, permissions=0o600):
    with open(path, 'a'):  # Create file if does not exist
        pass
    os.chmod(path, permissions)
    with open(path, 'w') as f:
        f.write(data)