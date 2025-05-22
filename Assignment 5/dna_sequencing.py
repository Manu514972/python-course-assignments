import sys

def clean_and_sort_dna(sequence):
    raw_segments = sequence.split('X')
    
    cleaned_segments = [seg for seg in raw_segments if seg and all(base in 'ACTG' for base in seg)]

    sorted_segments = sorted(cleaned_segments, key=len, reverse=True)

    return sorted_segments

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dna_sequencing.py <sequence>")
        sys.exit(1)

    input_sequence = sys.argv[1]
    result = clean_and_sort_dna(input_sequence)
    print(result)
