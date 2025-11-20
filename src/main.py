import json
import os
from snapshot import take_snapshot
from diff import diff_snapshots
from file_compare import file_status

SNAPSHOT_FOLDER = "snapshots"

def load_snapshot(path):
    with open(path) as f:
        return json.load(f)

def menu():
    print("\n====== FILE SYSTEM SNAPSHOT DIFF ======")
    print("1. Take Snapshot")
    print("2. Compare 2 Snapshots")
    print("3. Compare 2 Files")
    print("4. Exit")
    print("=======================================")

def main():
    os.makedirs(SNAPSHOT_FOLDER, exist_ok=True)

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            folder = input("Enter folder to snapshot: ")
            name = input("Snapshot name: ")
            output = f"{SNAPSHOT_FOLDER}/{name}.json"
            take_snapshot(folder, output)

        elif choice == "2":
            snap1 = input("Enter snapshot 1 name: ")
            snap2 = input("Enter snapshot 2 name: ")
            path1 = f"{SNAPSHOT_FOLDER}/{snap1}.json"
            path2 = f"{SNAPSHOT_FOLDER}/{snap2}.json"

            s1 = load_snapshot(path1)
            s2 = load_snapshot(path2)

            added, removed, modified = diff_snapshots(s1, s2)
            print("\n--- DIFF RESULT ---")
            print("Added:", added)
            print("Removed:", removed)
            print("Modified:", modified)

        elif choice == "3":
            old_file = input("Old file path: ")
            new_file = input("New file path: ")
            print("Status:", file_status(old_file, new_file))

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
