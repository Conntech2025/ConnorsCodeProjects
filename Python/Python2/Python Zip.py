import zipfile
import os

# Define source folder and zip file path
source_folder = r"C:/Users/stoic/OneDrive/Desktop/Python2"
zip_file_path = os.path.join(source_folder, "assignments.zip")

# List of all assignment files
files_to_zip = [
    "Understanding the tkinter window and how to use widgets.py",
    "Setting and getting widget data in tkinter.py",
    "Understanding Tkinter Variables.py",
    "An overview of the tkinter buttons (+using them with vraibles).py",
    "Using button functions with arguments in tkinter.py",
    "Understanding tkinter events.py",
    "The tkinter combobox and spinbox widgets.py",
    "creating tables in tkinter with the treeview widget.py",
    "Understanding parenting and frames in tkinter.py",
    "Tabs in Tkinter.py"
]

# Create a zip file and add files to it
with zipfile.ZipFile(zip_file_path, 'w') as zipf:
    for file in files_to_zip:
        file_path = os.path.join(source_folder, file)
        zipf.write(file_path, os.path.basename(file_path))  # Store without full path

print(f"All assignments are zipped into {zip_file_path}")
