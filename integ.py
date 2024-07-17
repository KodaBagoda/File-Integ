import os
import hashlib
from typing import Dict

def calculate_sha256(file_path: str) -> str:
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for data in iter(lambda: f.read(8192), b''):
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

def check_integrity(directory_path: str) -> None:
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Invalid directory path.")
        return
    
    file_hashes: Dict[str, str] = {}
    with os.scandir(directory_path) as entries:
        for entry in entries:
            if entry.is_file():
                file_path = entry.path
                calculated_hash = calculate_sha256(file_path)
                file_hashes[file_path] = calculated_hash
                print(f"File: {file_path}\n SHA-256 Hash: {calculated_hash}")
    
    # You can use the file_hashes dictionary for further processing or comparison
    # For example, compare hashes between different directories or check for changes

if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to check: ")
    check_integrity(directory_to_check)
