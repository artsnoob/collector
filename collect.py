import os

def collect_file_contents(folder_path, include_subfolders=False):
    # Create the output file path
    output_file = os.path.join(folder_path, "collection.txt")
    
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Iterate through all files in the folder and its subfolders
        for root, dirs, files in os.walk(folder_path):
            if root != folder_path and not include_subfolders:
                dirs.clear()  # This prevents os.walk from recursing into subfolders
                continue
            
            for filename in files:
                if filename != "collection.txt":
                    file_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(file_path, folder_path)
                    
                    try:
                        # Open and read the contents of each file
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                        
                        # Write the relative path and content to the output file
                        outfile.write(f"### {relative_path} ###\n\n")
                        outfile.write(content)
                        outfile.write("\n\n")
                        outfile.write("="*50)  # Separator
                        outfile.write("\n\n")
                    except Exception as e:
                        print(f"Error reading {relative_path}: {str(e)}")

    print(f"Collection saved to {output_file}")

# Get folder path from user
folder_path = input("Enter the folder path: ")

# Check if the folder exists
if os.path.isdir(folder_path):
    # Check for subfolders
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    
    if subfolders:
        include_subfolders = input("Subfolders detected. Do you want to include them? (y/n): ").lower() == 'y'
    else:
        include_subfolders = False
    
    collect_file_contents(folder_path, include_subfolders)
else:
    print("Invalid folder path. Please try again.")
