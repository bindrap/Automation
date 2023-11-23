import os
import shutil

source_folder = r"C:\Users\bindrap\Downloads"
destination_folder = r"G:\MoveTest_Parteek"
file_name_prefix = "Issued permits"

# List all files in the source folder
files = os.listdir(source_folder)

# List all files that start with file_name_prefix
matching_files = [f for f in files if f.startswith(file_name_prefix)]

# Sort the matching files by date
matching_files.sort()

if matching_files:
    most_recent_file = matching_files[-1]
    source_path = os.path.join(source_folder, most_recent_file)
    destination_path = os.path.join(destination_folder, most_recent_file)

    try:
        # Move the most recent file
        shutil.move(source_path, destination_path)
        print(f"File '{most_recent_file}' moved successfully from {source_path} to {destination_path}")
    except FileNotFoundError:
        print(f"Source file '{most_recent_file}' not found.")
    except PermissionError:
        print(f"Permission denied to move the file '{most_recent_file}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
else:
    print("No matching files found.")
