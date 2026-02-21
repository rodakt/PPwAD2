import os

path = "/home/tomek/Dokumenty/PPwAD2"

if not os.path.exists(path):
    print("Path does not exist")
    exit()

for root, dirs, files in os.walk(path):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, "rb") as f:
            size = len(f.read())
        print(f"{file_path} - {size} bytes")
        