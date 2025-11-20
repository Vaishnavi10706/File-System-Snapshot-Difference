import os
import hashlib
import json

def get_file_hash(path):
    hasher = hashlib.md5()
    with open(path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def take_snapshot(folder_path, output_file):
    snapshot = {"files": {}}

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, folder_path)

            stat = os.stat(full_path)
            file_hash = get_file_hash(full_path)

            snapshot["files"][rel_path] = {
                "size": stat.st_size,
                "mtime": stat.st_mtime,
                "hash": file_hash
            }

    with open(output_file, "w") as f:
        json.dump(snapshot, f, indent=4)

    print(f"[✔] Snapshot saved to {output_file}")
