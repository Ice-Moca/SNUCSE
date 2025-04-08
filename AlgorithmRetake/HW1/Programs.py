import random
import os
import sys
sys.setrecursionlimit(10**6)

    
def read_input(filepath):
    # read data from the input file
    with open(filepath, 'r') as f:
        arr = [int(line.strip()) for line in f]
    return arr

def generate_example_input1(filepath, n):
    """Generate an example input file with random numbers."""
    # Generate a list of random numbers between 1 and n/2
    with open(filepath, 'w') as f:
        for _ in range(n):
            f.write(f"{random.randint(1, n // 2)}\n")

def generate_example_input2(filepath, n):
    """Generate an example input file with random numbers."""
    # Generate a list of random numbers between 1 and n*2
    with open(filepath, 'w') as f:
        for _ in range(n):
            f.write(f"{random.randint(1, n * 2)}\n")

def write_output_file(filepath, n, i, arr):
    """Write the output file with n, i, and array values."""
    with open(filepath, 'w') as f:
        f.write(f"{n} {i}\n")  # Write n and i separated by a space
        f.write(' '.join(map(str, arr)) + '\n')  # Write array values separated by spaces

def main():
    # Ask the user if they want to process the new files
    proceed = input("Do you want to process the new files? (yes/no): ").strip().lower()
    if proceed != "yes":
        print("Skipping file generation. Using existing files if available.")
        base_dir = os.path.dirname(__file__)
        input_filepath1 = os.path.join(base_dir, "example_input1.txt")
        input_filepath2 = os.path.join(base_dir, "example_input2.txt")
    else:
        # Prompt user for the value of n
        try:
            n = int(input("Enter the value of n (number of random numbers to generate): "))
            print(f"Received input: {n}")  # 디버깅용 출력
            
            if n <= 0:
                print("Please enter a positive integer.")
                return
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return
        
        # Generate example input files
        print("Generating example input files...\n")
        base_dir = os.path.dirname(__file__) 

        # Filepath for generate_example_input1
        input_filepath1 = os.path.join(base_dir, "example_input1.txt")
        generate_example_input1(input_filepath1, n)
        print(f"Example input file 1 generated at: {input_filepath1}")

        # Filepath for generate_example_input2
        input_filepath2 = os.path.join(base_dir, "example_input2.txt")
        generate_example_input2(input_filepath2, n)
        print(f"Example input file 2 generated at: {input_filepath2}")
    
    # Process each example input file
    for input_filepath in [input_filepath1, input_filepath2]:
        print(f"\nProcessing file: {input_filepath}")
        
        # Ensure the input file exists
        if not os.path.exists(input_filepath):
            print(f"Input file not found: {input_filepath}")
            continue

        # (1) Read all input data into memory.
        arr = read_input(input_filepath)
        
        # Ask the user if they want to input `i` manually or generate it randomly
        i_choice = input("Do you want to input `i` manually? (yes/no): ").strip().lower()
        if i_choice == "yes":
            try:
                i = int(input(f"Enter the value of i (1 <= i <= {len(arr)}): "))
                if i < 1 or i > len(arr):
                    print(f"Invalid input. Please enter a value between 1 and {len(arr)}.")
                    continue
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
        else:
            i = random.randint(1, len(arr))  # Select a random i within the range of the array
            print(f"Randomly selected i: {i}")
        
        # Write the output file for example_input1
        output_filepath1 = os.path.join(base_dir, "example_input1.in")
        write_output_file(output_filepath1, n, i, arr)
        print(f"Output file generated at: {output_filepath1}")

        # Generate different content for example_input2
        arr2 = [random.randint(1, n * 2) for _ in range(n)]
        output_filepath2 = os.path.join(base_dir, "example_input2.in")
        write_output_file(output_filepath2, n, i, arr2)
        print(f"Output file generated at: {output_filepath2}")
    
if __name__ == "__main__":
    main()