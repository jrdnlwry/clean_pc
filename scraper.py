"""
Currently deprecated
"""
import os
import datetime
import csv

# Adjust this path to your actual Downloads directory
downloads_path = r"C:\Users\tatel\Downloads"
file_path = r"C:\Users\tatel\OneDrive\Documents\python\clean_pc"

# List to hold file metadata dictionaries
file_metadata_list = []

for filename in os.listdir(downloads_path):
    full_path = os.path.join(downloads_path, filename)

    # Check if it’s a file (not a directory)
    if os.path.isfile(full_path):
        # Gather file stats
        file_stat = os.stat(full_path)

        # Extract file extension/type
        # If there's no dot in the filename, extension will be empty
        file_ext = os.path.splitext(filename)[1].lstrip('.').lower()

        # Convert timestamps to human-readable dates
        created = datetime.datetime.fromtimestamp(file_stat.st_ctime).strftime("%B %d, %Y")
        modified = datetime.datetime.fromtimestamp(file_stat.st_mtime).strftime("%B %d, %Y")
        accessed = datetime.datetime.fromtimestamp(file_stat.st_atime).strftime("%B %d, %Y")

        # File size in bytes
        size = file_stat.st_size

        # Directory location (downloads_path)
        location = downloads_path

        # Store the file’s metadata
        file_data = {
            "file": full_path,
            "name": os.path.splitext(filename)[0],
            "type": file_ext,
            "location": location,
            "size (bytes)": size,
            "created": created,
            "modified": modified,
            "accessed": accessed
        }

        file_metadata_list.append(file_data)

# Define the CSV file path/name
csv_file_path = os.path.join(file_path, "file_metadata.csv")

# Write to CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["file", "name", "type", "location", "size (bytes)", "created", "modified", "accessed"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write all rows
    writer.writerows(file_metadata_list)

print(f"Metadata has been exported to {csv_file_path}")