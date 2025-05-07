import os
import fnmatch

def collect_file_contents(folder_path, include_subfolders=False, exclude_dirs=None, exclude_files=None):
    # Initialize empty lists if None is provided
    exclude_dirs = exclude_dirs or []
    exclude_files = exclude_files or []
    # Create the output file path
    output_file = os.path.join(folder_path, "collection.txt")
    
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Iterate through all files in the folder and its subfolders
        for root, dirs, files in os.walk(folder_path):
            if root != folder_path and not include_subfolders:
                dirs.clear()  # This prevents os.walk from recursing into subfolders
                continue
            
            # Filter out excluded directories
            for exclude_pattern in exclude_dirs:
                dirs[:] = [d for d in dirs if not fnmatch.fnmatch(d, exclude_pattern)]
            
            for filename in files:
                # Skip collection.txt and excluded files
                if filename != "collection.txt" and not any(fnmatch.fnmatch(filename, pattern) for pattern in exclude_files):
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
    # List top-level directories in the folder
    print("\nAvailable top-level directories in the selected folder:")
    print("="*50)
    
    # Get all items in the directory
    all_items = os.listdir(folder_path)
    directories = [item for item in all_items if os.path.isdir(os.path.join(folder_path, item))]
    
    # Display directories
    if directories:
        for directory in sorted(directories):
            print(f"  - {directory}")
    else:
        print("  No directories found.")
    
    print("="*50)
    
    # Check for subfolders
    if directories:
        include_subfolders = input("\nSubfolders detected. Do you want to include them? (y/n): ").lower() == 'y'
    else:
        include_subfolders = False
    
    # Get exclusion patterns
    print("\nYou can use wildcards like * and ? in your exclusion patterns.")
    print("Examples: 'node_modules' to exclude exact match, '*.log' to exclude all log files")
    exclude_dirs_input = input("\nEnter directories to exclude (comma-separated, leave empty for none): ")
    exclude_files_input = input("Enter files to exclude (comma-separated, leave empty for none): ")
    
    # Process exclusion inputs
    exclude_dirs = [pattern.strip() for pattern in exclude_dirs_input.split(',')] if exclude_dirs_input.strip() else []
    exclude_files = [pattern.strip() for pattern in exclude_files_input.split(',')] if exclude_files_input.strip() else []
    
    collect_file_contents(folder_path, include_subfolders, exclude_dirs, exclude_files)
else:
    print("Invalid folder path. Please try again.")
