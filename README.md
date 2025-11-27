File System Snapshot Diff

A Python-based tool that captures snapshots of a folder and compares them to show which files were added, modified, or removed.
The project also includes a Streamlit Web UI to make it easy to use from the browser for the user.

Features

1. File Snapshot Generation

a. Takes a complete snapshot of a folder at a particular time.

b. Stores file details (path + hash) in a JSON file.

c. Helps track changes between different snapshot versions.

2. Snapshot Comparison (Diff Tool)

Compares Snapshot A with Snapshot B and shows:

🟢 Added Files: New files present in Snapshot B but not in A

🟡 Modified Files: Files whose content has changed (identified using MD5 hash)

🔴 Removed Files: Files present in Snapshot A but missing in Snapshot B

3. Streamlit Web UI

A user-friendly interface built using Streamlit that allows users to:

Enter folder for snapshot

Generate snapshot files

Enter snapshot files name and compare snapshots

View results clearly: added, modified, and removed files

📂 Folder Structure

file-system-snapshot-diff/
│
├── snapshots/ # Auto-generated snapshot files
│
├── src/
| |-- init.py
│ ├── snapshot.py # Logic for taking snapshots
│ ├── diff.py # Logic for comparing snapshots
│ ├── file-compare.py # Hashing and helper functions
| |-- main.py
├── app.py # Streamlit Web UI
│--LICENSE #MIT license
└── README.md

Tech Stack

1. Python 3

2. Streamlit (for web UI)

3. JSON (to store snapshot data)

4. Hashlib MD5 (to detect changes in file content)

How It Works in Streamlit

How to open streamlit UI
streamlit run app.py

Step 1: Take a Snapshot
a. Enter folder name whose snapshot should be taken
b. Enter snapshot name
c. Click on take snapshot button

Step 2: Compare Two Snapshots
a. Enter the snap1 file
b. Enter the snap2 file
c. Click on compare snapshot button

Output Example

Added Files:

- test2.txt

Modified Files:

- README.md
- text1.txt

Removed Files:

- test3.txt

Purpose of the Project

This OJT project helps students understand:

How file systems work

How hashing helps detect content changes

How to build a real-world tool

How to integrate backend + UI

How to design clean folder structures and workflows
