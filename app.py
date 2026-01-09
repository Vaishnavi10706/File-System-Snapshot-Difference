import streamlit as st
import os
import json
import sys
import datetime

sys.path.append(os.path.join(os.getcwd(), "src"))

from snapshot import take_snapshot
from diff import diff_snapshots
from file_compare import file_status

SNAPSHOT_FOLDER = "snapshots"
os.makedirs(SNAPSHOT_FOLDER, exist_ok=True)

def load_snapshot(path):
    with open(path) as f:
        return json.load(f)

def get_snapshot_history():
    history = []

    for file in os.listdir(SNAPSHOT_FOLDER):
        if file.endswith(".json"):
            path = os.path.join(SNAPSHOT_FOLDER,file)
            created_time = os.path.getctime(path)
            created_time = datetime.datetime.fromtimestamp(created_time)

            with open(path,"r") as f:
                data = json.load(f)
            if isinstance(data,dict) and "files" in data:
                total_files = len(data["files"])
            else:
                total_files = len(data)
            history.append({
                "Snapshot Name": file.replace(".json",""),
                "Date/Time": created_time.strftime("%Y-%m-%d %H-%M:%S"),
                "Total Files": total_files
            })
    return history

def delete_snapshot(snapshot_name):
    path = os.path.join(SNAPSHOT_FOLDER,f"{snapshot_name}.json")
    if os.path.exists(path):
        os.remove(path)
        return True
    else:
        return False
    
def get_folder_statistics(folder_path):
    total_files = 0
    total_folders = 0
    last_modified = 0

    for root, dirs, files in os.walk(folder_path):
        total_folders += len(dirs)
        total_files += len(files)

        for f in files:
            file_path = os.path.join(root, f)
            try:
                last_modified = max(last_modified, os.path.getmtime(file_path))
            except:
                pass

    return total_files, total_folders, last_modified

def set_dark_mode():
    st.markdown("""
        <style>
        .stApp {
            background-color: #0d1117 !important;
            color: #ffffff !important;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: white !important;
        }
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #161b22 !important;
        }
        /* Buttons */
        .stButton>button {
            background-color: #238636 !important;
            color: white !important;
            border-radius: 8px;
            border: none;
        }
        .stTextInput>div>div>input,
        .stTextArea textarea {
            background-color: #ffffff10 !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

def set_light_mode():
    st.markdown("""
        <style>
        .stApp {
            background-color: white !important;
            color: black !important;
        }

        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
        }

        .stButton>button {
            background-color: black !important;
            color: white !important;
            border-radius: 8px;
            border: none;
        }
        </style>
    """, unsafe_allow_html=True)

st.title("FILE SYSTEM SNAPSHOT DIFFERENCE")

with st.sidebar:
  st.header("Settings")
  toggle_value = st.toggle("Dark Mode")
if toggle_value:
    set_dark_mode()
else:
    set_light_mode()

st.write("A simple web app UI for taking Snapshots , comparing two Snapshots and comparing two file changes.")

menu = st.sidebar.radio("Select an action", ["Take Snapshot","Snapshot History", "Compare Snapshots", "Compare Files"])

if menu == "Take Snapshot":
    st.header("Take snapshot of a folder")

    folder = st.text_input("Enter folder path to snapshot:")

    if folder and os.path.exists(folder):
        try:
            files, folders, last_modified = get_folder_statistics(folder)

            st.subheader("📁 Folder Statistics")
            st.info(f"""
**Total Files:** {files}  
**Total Folders:** {folders}    
**Last Modified:** {datetime.datetime.fromtimestamp(last_modified)}
            """)
        except Exception as e:
            st.error(f"Error reading folder: {e}")
    elif folder:
        st.error("Folder does not exist.")
        
    snap_name = st.text_input("Snapshot name (without extension):")

    if st.button("Take snapshot"):
        if not folder or not snap_name:
            st.error("Please provide both folder path and snapshot name.")
        else:
            output = f"{SNAPSHOT_FOLDER}/{snap_name}.json"

            try:
                take_snapshot(folder, output)
                st.success(f"✅ Snapshot saved to **{output}**")
            except Exception as e:
                st.error(f"Error: {e}")

elif menu == "Snapshot History":
    st.header("Snapshot History")
    history = get_snapshot_history()
    if not history:
        st.info("No Snapshot found.")
    else:
        col1,col2,col3,col4 = st.columns([3,3,2,1])
        col1.markdown("**Snapshot Name**")
        col2.markdown("**Date/Time**")
        col3.markdown("**Total Files**")
        col4.markdown("**Delete**")

        st.divider()

        for snap in history:
            c1,c2,c3,c4 = st.columns([3,3,2,1])

            c1.write(snap["Snapshot Name"])
            c2.write(snap["Date/Time"])
            c3.write(snap["Total Files"])

            if c4.button("🗙",key=f"del_{snap["Snapshot Name"]}"):
                if delete_snapshot(snap["Snapshot Name"]):
                    st.success(f"Deletef snapshot: {snap["Snapshot Name"]}")
                    st.rerun()
                else:
                    st.error("Failed to delete snapshot.")

elif menu == "Compare Snapshots":
    st.header("Compare two Snapshots")

    snap1 = st.text_input("Snapshot 1 name (without .json): ")
    snap2 = st.text_input("Snapshot 2 name (without .json): ")

    if st.button("Compare Snapshots"):
        try:
            path1 = f"{SNAPSHOT_FOLDER}/{snap1}.json"
            path2 = f"{SNAPSHOT_FOLDER}/{snap2}.json"

            s1 = load_snapshot(path1)
            s2 = load_snapshot(path2)

            added, removed, modified = diff_snapshots(s1, s2)

            st.subheader("Added Files")
            st.write(added or "None")

            st.subheader("Removed Files")
            st.write(removed or "None")

            st.subheader("Modified Files")
            st.write(modified or "None")

        except FileNotFoundError:
            st.error(" One or both snapshots do not exist.")
        except Exception as e:
            st.error(f"Error: {e}")

elif menu == "Compare Files":
    st.header("Compare Two Individual Files")

    old_file = st.text_input("Old file path:")
    new_file = st.text_input("New file path:")

    if st.button("Compare Files"):
        try:
            status = file_status(old_file, new_file)
            st.info(f"Result: **{status}**")
        except Exception as e:
            st.error(f"Error: {e}")
