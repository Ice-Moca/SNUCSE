import random
import sys
import os
sys.setrecursionlimit(10**6)

def generate_example_input(filepath):
    """Generate an example input file with random numbers."""
    with open(filepath, 'w') as f:
        for _ in range(100000):
            f.write(f"{random.randint(1, 50000)}\n")
def main():
    # Generate example input file
    base_dir = os.path.dirname(__file__) 
    input_filepath = os.path.join(base_dir, "example_input.txt")
    generate_example_input(input_filepath)

if __name__ == "__main__":
    main()
    