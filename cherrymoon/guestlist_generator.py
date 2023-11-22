import random
import string

def generate_guestlist_codes(prefix, num_codes=50, code_length=4):
    guestlist_codes = []
    for _ in range(num_codes):
        # Generate the random code with the prefix, using lowercase letters only
        code = prefix + ''.join(random.choices(string.ascii_lowercase + string.digits, k=code_length))
        guestlist_codes.append(code)
    return guestlist_codes

def write_to_file(file_path, codes):
    with open(file_path, 'w') as file:
        for code in codes:
            file.write(f"{code}\n")

if __name__ == "__main__":
    # Prefix for the Guestlist Codes
    code_prefix = "cherrymoon-"

    # Number of codes to generate
    num_codes_to_generate = 50

    # Call the function to generate the Guestlist Codes with prefix
    generated_codes = generate_guestlist_codes(code_prefix, num_codes=num_codes_to_generate)

    # Output the generated codes to the console
    print(f"Generated {num_codes_to_generate} Guestlist Codes with Prefix '{code_prefix}':")
    for i, code in enumerate(generated_codes, start=1):
        print(f"{i}. {code}")

    # File path for the text file
    file_path = "guestlist_codes.txt"

    # Write the generated codes to the text file
    write_to_file(file_path, generated_codes)

    print(f"Guestlist Codes have been written to the file '{file_path}'.")