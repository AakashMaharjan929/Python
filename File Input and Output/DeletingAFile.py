# Deleting a file in Python

import os

f = open("tempfile.txt", "w")
f.write("This is a temporary file that will be deleted.")
f.close()

# Check if the file exists before deleting
if os.path.exists("tempfile.txt"):
    os.remove("tempfile.txt")
    print("tempfile.txt has been deleted.")
else:
    print("tempfile.txt does not exist.")