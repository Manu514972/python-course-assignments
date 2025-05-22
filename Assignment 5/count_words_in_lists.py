from collections import Counter

celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]

def count_words(words):
    word_counts = Counter(words)

    for word, count in word_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    count_words(celestial_objects)
