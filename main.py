import os

base = os.path.dirname("index.html")
file_path = os.path.join("folder","index.html")

with open(file_path,"r") as f:
  print(f.read())