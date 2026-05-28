import sys
from src import generate_seed_phrase, validate_seed_phrase

def main():
    try:
        strength = int(sys.argv[1]) if len(sys.argv) > 1 else 128
        phrase = generate_seed_phrase(strength=strength)
        print(f"Seed phrase ({len(phrase.split())} words):")
        print(phrase)
        print(f"\nValid: {validate_seed_phrase(phrase)}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()