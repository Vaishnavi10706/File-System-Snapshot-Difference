File System Snapshot Diff

A Python-based tool that captures snapshots of a folder and compares them to show which files were added, modified, or removed.

The project also includes a Streamlit Web UI to make it easy for users to interact with the system from the browser.

Features

1. File Snapshot Generation

Takes a complete snapshot of a folder at a particular time.

Stores file details (path + MD5 hash) in a JSON file.

Helps track changes between multiple snapshot versions.

2. Snapshot Comparison (Diff Tool)

The tool compares Snapshot A with Snapshot B and displays:

🟢 Added Files: New files present in Snapshot B but not in Snapshot A

🟡 Modified Files: Files whose content has changed (detected using MD5 hash)

🔴 Removed Files: Files present in Snapshot A but missing in Snapshot B

3. Streamlit Web UI

A user-friendly UI built with Streamlit that allows users to:

Enter folder name for snapshot

Generate snapshot files

Enter snapshot file names and compare snapshots

Clearly view results: added, modified, and removed files

Folder Structure

```
FILE-SYSTEM-SNAPSHOT-DIFF/
│
├── folder/ # Sample folder for testing (contains text.txt)
│
├── snapshots/ # Auto-generated snapshot files (JSON)
│
├── src/
│ ├── **pycache**/ # Python cache files
│ ├── diff.py # Compares two snapshots and finds added/modified/removed files
│ ├── file_compare.py # Line-by-line comparison for modified files
│ ├── main.py # Main logic (Streamlit backend functions)
│ ├── snapshot.py # Takes snapshot of the folder (creates JSON)
│
├── app.py # Streamlit Web UI entry file
│
├── LICENSE # License for the project
├── README.md # Project documentation
└── requirements.txt # Python dependencies (Streamlit, etc.)
```

Tech Stack

Python 3

Streamlit (for Web UI)

JSON (to store snapshot data)

Hashlib MD5 (to detect file content changes)

How It Works in Streamlit
How to open Streamlit UI
streamlit run app.py

Step 1: Take a Snapshot

Enter the folder name whose snapshot should be taken

Enter the snapshot name

Click on Take Snapshot

Step 2: Compare Two Snapshots

Enter the first snapshot file

Enter the second snapshot file

Click on Compare Snapshots

Output Example

Added Files

test2.txt

Modified Files

README.md

text1.txt

Removed Files

test3.txt

Purpose of the Project

This OJT project helps students understand:

How file systems work

How hashing helps detect content changes

How to build a real-world tool

How to integrate backend + UI

How to design clean folder structures and workflows

```

```
