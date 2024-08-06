# File Content Collector

This Python script collects the contents of all files in a specified folder and combines them into a single text file. It's designed to make it easier to add multiple files to an LLM (Large Language Model) conversation by consolidating them into one file.

## Features

- Scans all files in a specified folder
- Creates a new file called `collection.txt` in the same folder
- Writes the contents of each file to `collection.txt`
- Clearly separates each file's content with the filename and a separator
- Handles potential encoding issues
- Skips the `collection.txt` file itself to avoid recursive inclusion

## Requirements

- Python 3.x

## Usage

1. Save the script as `collector.py` in your desired location.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:

   ```
   python collector.py
   ```

5. When prompted, enter the full path to the folder containing the files you want to collect.

The script will create a `collection.txt` file in the specified folder, containing the contents of all other files in that folder.

## Example

```
$ python file_collector.py
Enter the folder path: /path/to/your/folder
Collection saved to /path/to/your/folder/collection.txt
```

## Output Format

The `collection.txt` file will have the following format:

```
### filename1.ext ###

[Contents of filename1.ext]

==================================================

### filename2.ext ###

[Contents of filename2.ext]

==================================================

[... and so on for each file in the folder]
```

## Notes

- The script attempts to read all files with UTF-8 encoding. If a file cannot be read, an error message will be printed, and the script will continue with the next file.
- Binary files or files with non-text content may not be processed correctly and could result in errors or unreadable content in the output file.
- Large folders with many files or very large files may take some time to process.

## Contributing

Feel free to fork this repository and submit pull requests to enhance the functionality of this script. You could consider adding features such as:

- Command-line arguments for folder path
- Options to include/exclude specific file types
- Handling of subdirectories
- Custom output file naming
