import os
import glob

# Specify the folder containing the scraped files
folder_path = "data"  # Update with the path to your folder

# Delete all files in the specified folder
files = glob.glob(os.path.join(folder_path, '*'))
for f in files:
    try:
        os.remove(f)
        print(f"Deleted: {f}")
    except Exception as e:
        print(f"Error deleting {f}: {e}")

print("All scraped files have been deleted.")
