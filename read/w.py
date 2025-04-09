def read_and_write_file():
    import os

    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Define the output filename
        output_filename = f"modified_{os.path.basename(input_filename)}"

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_write_file()