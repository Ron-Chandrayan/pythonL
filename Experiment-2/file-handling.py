''' File Handling:
- Text file processing
- Display count of no of lines
- No of words
- No of characters in the file '''

def file_statistics(filename):
    line_count = 0
    word_count = 0
    char_count = 0

    try:
        with open(filename, "r") as f:
            for line in f:
                line_count += 1
                words = line.split()
                word_count += len(words)
                char_count += len(line)  # includes spaces + newline

        print(f"\nFile: {filename}")
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {char_count}")

    except FileNotFoundError:
        print("File not found. Please check the filename.")

filename = input("Enter the filename: ")
file_statistics(filename)
