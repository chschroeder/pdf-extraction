import re
import os

# Read the log file
log_file = "/disk1/users/mbehret/output_dissertations.log"

processed_files_file = "/disk1/users/mbehret/PycharmProjects/pdf-extraction/processed_files.txt"

# Load processed filenames if the file exists
processed_files = set()
if os.path.exists(processed_files_file):
    with open(processed_files_file, "r") as f:
        processed_files = set(f.read().splitlines())

# Extract processed PDF filenames from the log file
processed_filenames = set()
with open(log_file, "r") as f:
    for line in f:
        match = re.search(r"processing pdf file (\S+\.pdf)", line)
        if match:
            pdf_filename = match.group(1)
            processed_filenames.add(pdf_filename)

# Append the processed filenames to the set of processed files
processed_files.update(processed_filenames)

# Write the updated set of processed filenames back to the processed_files.txt file
with open(processed_files_file, "w") as f:
    for filename in processed_files:
        f.write(filename + "\n")