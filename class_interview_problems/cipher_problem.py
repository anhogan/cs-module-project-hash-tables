
# Goal: write an encode() function to scramble a string it's given
# Need to change one character into another
# Map from one character to another
# Use that to change an entire string into another

encode_table = {
  "A": "M",
  "B": "N",
  "C": "B",
  "D": "V",
  "E": "C",
  "F": "X",
  "G": "Z",
  "H": "L",
  "I": "K",
  "J": "J",
  "K": "H",
  "L": "G",
  "M": "F",
  "N": "D",
  "O": "S",
  "P": "A",
  "Q": "P",
  "R": "O",
  "S": "I",
  "T": "U",
  "U": "Y",
  "V": "T",
  "W": "R",
  "X": "E",
  "Y": "W",
  "Z": "Q"
}

decode_table = {}

# Decode_table = {v:k for k, v in encode_table.items()} 
def build_decode(encoding_table):
    for key, value in encoding_table.items():
        decode_table[value] = key

def decode(s):
    decoded_string = ""
    for character in s:
        if character not in decode_table:
            decoded_string += character
        else:
            # For each character, look up its mapping
            unscrambled_character = decode_table[character]
            # Build our return string
            decoded_string += unscrambled_character

    return decoded_string

def encode(s):
    encoded_string = ""

    # Iterate over the given string
    s = s.upper()
    for character in s:
        if character not in encode_table:
            encoded_string += character
        else:
            # For each character, look up its mapping
            scrambled_character = encode_table[character]
            # Build our return string
            encoded_string += scrambled_character

    return encoded_string

encoded = encode("Hail Caesar, we who are about to die salute thee")
print(encoded)
build_decode()
decoded = decode(encoded)
print(decoded)

# Review
## What gave me the most trouble, or took the longest?
## What concept or tool might have helped me?