File System Snapshot Difference

A Python-based tool that captures snapshots of a folder and compares them to show which files were added, modified, or removed.

The project now includes a Folder Statistics feature, which automatically displays useful information about any folder as soon as the user enters the folder name in the Streamlit UI.

A Streamlit Web UI makes it easy for users to interact with the tool directly from a browser.

Features:

1. File Snapshot Generation

Takes a complete snapshot of a selected folder

Stores file details (path + MD5 hash) in a JSON file

Helps track changes between two snapshot versions

2. Snapshot Comparison (Diff Tool)

Compares Snapshot A with Snapshot B and detects:

🟢 Added Files — Present in Snapshot B but missing in Snapshot A

🟡 Modified Files — Content changed (detected using MD5 hash)

🔴 Removed Files — Present in Snapshot A but not in Snapshot B

3. Folder Statistics (New Feature)

When the user enters a folder name and presses Enter, the app automatically displays:

- Total Files

- Total Folders

- Last Modified Time

This instant preview helps users understand the folder structure before taking a snapshot.

4. Streamlit Web UI

A clean and simple interface where users can:

Type a folder name -> Automatically see folder statistics

Enter a snapshot name -> Generate a new snapshot

Choose snapshot files -> Compare snapshots

View added, removed, modified files

5. Snapshot History table

A clean Table which shows all the snapshots in a table format which includes columns like Snapshot Name , Date/Time , No of file inside folder , confirmation checkbox (to confirm that if user actually wanted to delete the snapshot or not) and a delete button to delete the particular snapshot.

It helps the user to get a list of snapshots in one place so that the users can see which snapshot is added and which snapshot is deleted.

Folder Structure:

```
FILE-SYSTEM-SNAPSHOT-DIFFERENCE/
│
├── folder/ # Sample folder for testing(test.txt file)
│
├── snapshots/ # Auto-generated snapshot JSON files
│
├── src/
│ ├── **pycache**/ # Cache files
│ ├── diff.py # Compares two snapshots
│ ├── file_compare.py # Line-by-line comparison
│ ├── main.py # Streamlit backend functions
│ ├── snapshot.py # Snapshot generator
│
│
├── app.py # Streamlit UI entry point (folder statistics)
│
├── LICENSE
├── README.md
└── requirements.txt
```

Tech Stack Used:

Python 3

Streamlit

JSON

Hashlib MD5

OS

How to Use the Streamlit UI:

Run the app:

streamlit run app.py

Step 1: View Folder Statistics (New & Automatic)

Enter the folder name in the input field

Press Enter

The app automatically shows:

Total Files

Total Folders

Total Size

Last Modified Time

This happens before taking a snapshot.

Step 2: Take a Snapshot

Enter the snapshot name

Click Take Snapshot

A new JSON snapshot file is created inside the snapshots/ folder

Step 3: Compare Snapshots

Enter Snapshot A

Enter Snapshot B

Click Compare Snapshots

The UI will show:

Added files

Modified files

Removed files

Example Output:

Folder Statistics

Total Files: 1

Total Folders: 0

Last Modified: 2025-12-02 11:27:33

Snapshot Diff

Added Files:

test2.txt

Modified Files:

README.md

text1.txt

Removed Files:

test3.txt

Purpose of the Project:

This OJT project helps students learn:

How file systems store and update data

How hashing detects content changes

How to build real-world developer tools

How to integrate backend logic with Streamlit web UI

How to compute folder statistics and structure metadata

How to design clean and professional project architecture
