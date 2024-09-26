import os

# Function to count files in a directory and subdirectories, summing counts from child nodes
def count_files_in_directory(directory):
    total_files = 0
    subdirectory_counts = {}

    # Traverse the directory
    for root, dirs, files in os.walk(directory):
        # If we haven't visited this directory yet
        if root not in subdirectory_counts:
            subdirectory_counts[root] = len(files)

        # Add file count to current directory
        total_files += len(files)

        # Recursively count files in subdirectories
        for d in dirs:
            subdir_path = os.path.join(root, d)
            subdir_total = count_files_in_directory(subdir_path)[1]  # Get count from child directory
            subdirectory_counts[subdir_path] = subdir_total
            total_files += subdir_total

        break  # Break after first os.walk iteration since we handle recursion manually

    return subdirectory_counts, total_files

# Function to print the tree with file counts in each directory
def print_tree(directory, subdirectory_counts, level=0):
    # Get indentation based on the directory level (depth)
    indent = ' ' * 4 * level
    # Print the current directory and the total count of files (including subdirectories)
    print(f"{indent}{os.path.basename(directory)}/ - {subdirectory_counts[directory]} files")

    # Recursively print the subdirectories
    for subdirectory in subdirectory_counts:
        if os.path.dirname(subdirectory) == directory:
            print_tree(subdirectory, subdirectory_counts, level + 1)

# Directory to count files in
directory_path = '/path/to/directory'

# Get the file counts for the directory and all subdirectories
subdirectory_counts, total_file_count = count_files_in_directory(directory_path)

# Print the result in a tree format
print_tree(directory_path, subdirectory_counts)
