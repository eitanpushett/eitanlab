import os
import random
import string
import argparse

# Create an argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--prefix", type=str, default="file_", help="Prefix for the file names")
parser.add_argument("--suffix", type=str, default=".txt", help="Suffix for the file names")
parser.add_argument("--num_files", type=int, default=30000, help="Number of files to generate")
parser.add_argument("--file_size", type=int, default=100, help="Size of each file in KB")
parser.add_argument("--num_epochs", type=int, default=1, help="Number of epochs to run")
args = parser.parse_args()

# Generate and save the files for each epoch
for i in range(args.num_epochs):
    # Define the directory where the files will be saved for this epoch
    output_dir = "./epoch_" + str(i+1) + "/"
    
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate and save the files
    for j in range(args.num_files):
        # Generate a random filename
        filename = args.prefix + ''.join(random.choices(string.ascii_lowercase, k=10)) + args.suffix

        # Generate random data for the file
        data = ''.join(random.choices(string.ascii_letters + string.digits, k=args.file_size*1024))

        # Write the data to the file
        with open(output_dir + filename, 'w') as f:
            f.write(data)

        print("Generated file:", filename)

    print("Epoch", i+1, "done.")

print("All epochs done.")
