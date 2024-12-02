def count_file_content(filename):
    try:
        with open(filename) as file:
            lines = file.readlines()
            lines_count = len(lines)
            words_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)

            print(f"File name: {filename}")
            print(f"Number of lines: {lines_count}")
            print(f"Number of characters: {words_count}")
            print(f"Number of words: {char_count}")
    except FileNotFoundError:
        print(f'The file {filename} is not found')

count_file_content("files.txt")