#week6_strings


def encode_string(input_str):

    if not input_str.isprintable():
        return "Invalid input: only printable characters allowed."

    result = []
    i = 0

    while i < len(input_str):
        char = input_str[i]
        count = 1

        # Count times character repeats
        while i + 1 < len(input_str) and input_str[i + 1] == char:
            count += 1
            i += 1

        # Escape handling
        if char == '#':
            result.append('##')
        elif char.isdigit():
            result.append('#' + char)
        else:
            result.append(char)

        if count > 1:
            result.append(str(count))

        i += 1

    # Add a prefix 
    return "##00" + ''.join(result)

def decode_string(encoded_str):

    if not encoded_str.startswith("##00"):
        return "This string doesn't look encoded (missing ##00 prefix)."

    result = []
    i = 4  # skip past '##00'

    while i < len(encoded_str):
        char = encoded_str[i]

        if char == '#':
            i += 1
            if i < len(encoded_str):
                if encoded_str[i] == '#':
                    result.append('#')
                else:
                    result.append(encoded_str[i])
        else:
            # Check for a number after the character
            j = i + 1
            count_str = ''
            while j < len(encoded_str) and encoded_str[j].isdigit():
                count_str += encoded_str[j]
                j += 1

            count = int(count_str) if count_str else 1
            result.extend([char] * count)
            i = j - 1

        i += 1

    return ''.join(result)

def main():
    print("Welcome to the Run-Length Encoder/Decoder!")
    choice = input("Type 'E' to encode or 'D' to decode a string: ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please type 'E' or 'D'.")
        return

    user_input = input("Enter your string: ").strip()

    if choice == 'E':
        encoded = encode_string(user_input)
        print("Encoded string:", encoded)
    else:
        decoded = decode_string(user_input)
        print("Decoded string:", decoded)

if __name__ == "__main__":
    main()
