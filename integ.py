import os
import hashlib
from typing import Dict, Tuple

def calculate_sha256(file_path: str) -> str:
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for data in iter(lambda: f.read(8192), b''):
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

def get_file_size(file_path: str) -> int:
    return os.path.getsize(file_path)

def check_integrity(directory_path: str) -> None:
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Invalid directory path.")
        return
    
    file_info: Dict[str, Tuple[int, str]] = {}
    with os.scandir(directory_path) as entries:
        for entry in entries:
            if entry.is_file():
                file_path = entry.path
                file_size = get_file_size(file_path)
                calculated_hash = calculate_sha256(file_path)
                file_info[file_path] = (file_size, calculated_hash)
                print(f"File: {file_path}\n Size: {file_size} bytes\n SHA-256 Hash: {calculated_hash}")
    
    # You can use the file_info dictionary for further processing or comparison
    # For example, compare file sizes and hashes between different directories or check for changes

if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to check: ")
    check_integrity(directory_to_check)
