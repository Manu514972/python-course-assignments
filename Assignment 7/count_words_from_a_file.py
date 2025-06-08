import sys
from collections import Counter
import re


def count_words_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)
            word_counts = Counter(words)
            for word, count in word_counts.items():
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_words_from_a_file.py <filename>")
    else:
        count_words_from_file(sys.argv[1])
