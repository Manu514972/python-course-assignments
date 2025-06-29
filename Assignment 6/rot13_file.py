import sys
import codecs
import os

def rot13_file(filepath):
    if not os.path.isfile(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        sys.exit(1)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    rot13_content = codecs.encode(content, 'rot_13')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(rot13_content)

    print(f"File '{filepath}' has been replaced with its ROT13 encoding.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python rot13_file.py <filename>")
        sys.exit(1)

    filepath = sys.argv[1]
    rot13_file(filepath)
