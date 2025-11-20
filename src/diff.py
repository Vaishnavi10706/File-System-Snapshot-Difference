import json

def diff_snapshots(old_snap, new_snap):
    old_files = old_snap["files"]
    new_files = new_snap["files"]

    added = []
    removed = []
    modified = []

    for file in new_files:
        if file not in old_files:
            added.append(file)
        else:
            if new_files[file]["hash"] != old_files[file]["hash"]:
                modified.append(file)

    for file in old_files:
        if file not in new_files:
            removed.append(file)

    return added, removed, modified