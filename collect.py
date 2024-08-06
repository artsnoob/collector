import os

def collect_file_contents(folder_path):
    # Create the output file path
    output_file = os.path.join(folder_path, "collection.txt")
    
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Iterate through all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Check if it's a file (not a directory)
            if os.path.isfile(file_path) and filename != "collection.txt":
                try:
                    # Open and read the contents of each file
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                    
                    # Write the filename and content to the output file
                    outfile.write(f"### {filename} ###\n\n")
                    outfile.write(content)
                    outfile.write("\n\n")
                    outfile.write("="*50)  # Separator
                    outfile.write("\n\n")
                except Exception as e:
                    print(f"Error reading {filename}: {str(e)}")

    print(f"Collection saved to {output_file}")

# Get folder path from user
folder_path = input("Enter the folder path: ")

# Check if the folder exists
if os.path.isdir(folder_path):
    collect_file_contents(folder_path)
else:
    print("Invalid folder path. Please try again.")