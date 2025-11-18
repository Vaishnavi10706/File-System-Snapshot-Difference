# File-System-Snapshot-Difference
This is our OJT Project in Product Development
File System Snapshot Diff:


TASK 1:
Take a snapshot of a folder and save file details (name, size, modified time);

take_snapshot()   scans a given folder recursively and records information about each file so that the folder’s state can be saved and compared later.

Inputs
•	folder_path (str): The folder you want to snapshot.
•	use_hash (bool, optional): If True, it calculates an MD5 hash for each file to detect content changes accurately.
What it Does
Walks through the folder using os.walk(), including all subfolders.
For each file, collects:
o	Size (st_size) – to detect changes in file length.
o	Modification time (st_mtime) – to detect when the file was last changed.
o	Optional hash (hash) – a fingerprint of the file content to detect content changes even if size or time doesn’t change.

Stores each file in a dictionary with its relative path as the key and file info as the value.

Skips files that can’t be accessed due to permissions or if they no longer exist.

Why It’s Feature One
This function collects all the data needed to represent the current state of a folder, which is the first step in your tracker. The snapshot is later saved to JSON with save_snapshot() for later comparison.


Feature Two: Compare Snapshots (Simple Explanation)
Feature Two is used to find changes in a folder by comparing two snapshots – an old one and a new one.
How it works:
1.	It checks which files are new (added), which are missing (deleted), and which are changed (modified).
2.	For modified files, it compares size, last modified time, or file content (if hash is used).
3.	After comparison, it shows the results in a report with:
o	+ for added
o	- for deleted
o	* for modified

Optional: You can also save the report to a CSV file.
Why it’s important:
•	This is the core part of folder tracking.
•	It tells exactly what changed in the folder since the last snapshot.
•	It uses the snapshot from Feature One to compare.




Feature Three: Export Results to CSV
Purpose:
This feature allows the user to save the folder changes report into a CSV file, which makes it easy to:
•	Share the report with others
•	Print the report
•	Analyze the changes in spreadsheet tools like Excel or Google Sheets


How it works (Code Implementation)
1.	Function: export_csv(added, deleted, modified, output_file)
o	Inputs:
	added → list of files that were added
	deleted → list of files that were deleted
	modified → list of files that were modified
	output_file → the path/name of the CSV file to save
2.	Process:
o	Open the CSV file for writing.
o	Write a header row: "Change Type", "File Path"
o	Loop through each list and write each file with its change type:
	Added → newly added files
	Deleted → removed files
	Modified → changed files
3.	Output:
o	A CSV file with two columns:
1.	Change Type → Added / Deleted / Modified
2.	File Path → relative path of the file
Why it’s useful
•	Shareable: You can send the CSV to colleagues or other users.
•	History tracking: Keeps a record of folder changes over time.
•	Analysis: Open in Excel, Google Sheets, or other tools to sort, filter, or analyze changes.
//

