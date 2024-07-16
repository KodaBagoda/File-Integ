## File Integrity Checker (Python)

This Python script uses SHA-256 hashing to verify the integrity of files within a directory. It calculates the SHA-256 hash of each file and displays it for comparison with known hashes or for tracking changes.

**Features:**

* Calculates SHA-256 hashes for files in a specified directory.
* Recursively walks through subdirectories to check all files.
* Validates user input for a directory path.
* Prints file paths and their corresponding SHA-256 hashes. 
* The `file_hashes` dictionary provides further processing or comparison options.

**Dependencies:**

* This project requires no external libraries and uses built-in Python modules:
    * `os` for file system interactions.
    * `hashlib` for SHA-256 hashing.

**Usage:**

1. Clone this repository.
2. Open a terminal and navigate to the project directory.
3. Run the script (`file_integrity_checker.py`) using `python file_integrity_checker.py`.
4. When prompted, enter the path to the directory you want to check.
5. The script will display the file paths and their SHA-256 hashes.

**Example Output:**

```
Enter the directory path to check: /path/to/your/directory/

File: /path/to/your/directory/file1.txt
 SHA-256 Hash: 38b060a75b5a0bd1e7d009ceda760a1c36c8fb455e4680526acc9c7c842c7e0b

File: /path/to/your/directory/subfolder/file2.jpg
 SHA-256 Hash: 9f86d081884c7d659a2feaa0c55ecd817ecac92034e6c6738c54fbee907f1e56
```

**Applications:**

* Verifying the integrity of downloaded files after transfer or storage.
* Creating a baseline hash database for sensitive files to detect modifications.
* Monitoring changes in file content over time (use `file_hashes` dictionary for comparison).

**Disclaimer:**

* SHA-256 does not guarantee file uniqueness, but collisions are very rare.
* This script calculates hashes for verification purposes. Securely storing and comparing hashes requires additional considerations.

**Contributing:**

Feel free to fork this repository and make improvements! Here are some ideas:

* Implement file size checks alongside SHA-256 hashes for additional verification.
* Allow users to specify a file extension filter to check specific file types.
* Add options to save calculated hashes to a file for record-keeping.
* Explore integrating with version control systems (optional).

**Security Considerations:**

* While SHA-256 is a secure hashing algorithm, the security of your files depends on how you manage the calculated hashes. Store them securely and avoid exposing them to unauthorized access.
