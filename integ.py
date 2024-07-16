import os
import hashlib

def calculate_sha256(file_path):
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

def check_integrity(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Invalid directory path.")
        return
    
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            calculated_hash = calculate_sha256(file_path)
            print(f"File: {file_path}\n SHA-256 Hash: {calculated_hash}")

if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to check: ")
    check_integrity(directory_to_check) 