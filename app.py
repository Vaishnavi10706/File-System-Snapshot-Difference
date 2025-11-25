import streamlit as st
import os
import json
import sys

sys.path.append(os.path.join(os.getcwd(),"src"))

from snapshot import take_snapshot

SNAPSHOT_FOLDER = "snapshots"
os.makedirs(SNAPSHOT_FOLDER,exist_ok=True)

def load_snapshot(path):
  with open(path) as f:
    return json.load(f)

st.title("FILE SYSTEM SNAPSHOT DIFFERENCE")
st.write("A simple web app UI for taking Snapshots , comparing two Snapshots and comparing two file changes.")

menu = st.sidebar.radio("Select an action",["Take Snapshot","Compare Snapshots","Compare Files"])

if menu == "Take Snapshot":
  st.header("Take snapshot of a folder")
  folder = st.text_input("Enter folder path to snapshot:")
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
