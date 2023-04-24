import os
import random
import string

# Define the number of files to generate
num_files = 30000

# Define the size of each file (in KB)
file_size = 100

# Define the directory where the files will be saved
output_dir = "cnvrg/output/"

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate and save the files
for i in range(num_files):
    # Generate a random filename
    filename = ''.join(random.choices(string.ascii_lowercase, k=10)) + ".txt"
    
    # Generate random data for the file
    data = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size*1024))
    
    # Write the data to the file
    with open(output_dir + filename, 'w') as f:
        f.write(data)
    
    print("Generated file:", filename)

print("Done.")
