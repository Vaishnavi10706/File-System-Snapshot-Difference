import os
import hashlib

def file_status(old_file, new_file):

    if not os.path.exists(old_file) and os.path.exists(new_file):
        return "ADDED"

    if os.path.exists(old_file) and not os.path.exists(new_file):
        return "REMOVED"

    if not os.path.exists(old_file) and not os.path.exists(new_file):
        return "BOTH FILES MISSING"

    def get_hash(p):
        h = hashlib.md5()
        with open(p, "rb") as f:
            h.update(f.read())
        return h.hexdigest()

    if get_hash(old_file) != get_hash(new_file):
        return "MODIFIED"
    else:
        return "NO CHANGE"