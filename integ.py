import os
import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for data in iter(lambda: f.read(8192), b''):
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

def check_integrity(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Invalid directory path.")
        return
    
    file_hashes = {}
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            calculated_hash = calculate_sha256(file_path)
            file_hashes[file_path] = calculated_hash
            print(f"File: {file_path}\n SHA-256 Hash: {calculated_hash}")
    
    # You can use the file_hashes dictionary for further processing or comparison
    # For example, compare hashes between different directories or check for changes

if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to check: ")
    check_integrity(directory_to_check) 