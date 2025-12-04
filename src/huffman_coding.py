from queue import PriorityQueue


def encode(msg: str) -> tuple[str, dict[str, str]]:
    """
    Encode string using Huffman coding algorithm.
    Return encoded string and dictionary containing codes.
    Key -> character, Value -> code.
    """

    class PriorityPair:
        """For priority queue pair implementation"""

        def __init__(self, priority, value):
            self.priority = priority
            self.value = value

        def __lt__(self, other: "PriorityPair"):
            return self.priority < other.priority

        # For debug purposes
        def __str__(self):
            return f"<!({self.priority})!, {self.value}>"

        # For debug purposes
        def __repr__(self):
            return f"<!({self.priority})!, {self.value}>"

    # Count frequences of characters.
    frequency = {}
    for ch in msg:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    # Edge case, when string consists of one type of characters.
    if len(frequency) == 1:
        return [len(msg) * "0", {msg[0]: "0"}]

    # Put frequences into priority queue.
    sorted_frequency = PriorityQueue()
    for i in frequency:
        item = PriorityPair(frequency[i], i)
        sorted_frequency.put(item)

    # Construct pseudo-binary tree sorted by frequences.
    # Wrap the characters together.
    while sorted_frequency.qsize() > 1:
        least1 = sorted_frequency.get()
        least2 = sorted_frequency.get()
        item = PriorityPair(least1.priority + least2.priority, (least1, least2))
        sorted_frequency.put(item)

    # Unwrap the characters and assign codes to them.
    codes = {}
    if not sorted_frequency.empty():
        codes[sorted_frequency.queue[0]] = ""

    while not sorted_frequency.empty():
        item = sorted_frequency.get()
        code = codes[item]
        # Basic case, when we get to the leaf.
        if isinstance(item.value, str):
            codes.pop(item)
            codes[item.value] = code
            continue
        # Else try to unwrap the node into two children.
        left = item.value[0]
        right = item.value[1]
        codes.pop(item)

        codes[left] = code + "0"
        codes[right] = code + "1"
        sorted_frequency.put(left)
        sorted_frequency.put(right)

    # Construct result encoded string.
    output_string = ""
    for ch in msg:
        output_string += codes[ch]
    return (output_string, codes)


def decode(codes: dict[str, str], msg: str) -> str:
    """
    Decode string with given codes.
    'codes' must contain character as key and code as value.
    Raises TypeError if undefined code was found.
    """

    # Reverse code table.
    char_table = {}
    for char in codes:
        char_table[codes[char]] = char

    output = ""
    start = 0
    end = 0
    while end < len(msg):
        if msg[start : end + 1] in char_table:
            output += char_table[msg[start : end + 1]]
            start = end + 1
        end += 1

    if start != end:
        raise TypeError(f"Undefined code: {msg[start:end]}. Failed to decode.")
    return output


def encode_fstr(file_in: str, file_out: str):
    """
    Encode file with name 'file_in' and
    write the result into file with name 'file_out'.
    """
    with open(file_in) as fin:
        data = fin.read()
        encoded_data, codes = encode(data)
        with open(file_out, "w") as fout:
            # Write file signature.
            fout.write("HC30\n")
            # Write codes.
            for ch in codes:
                # Wrap escape sequences.
                fout.write(repr(ch) + "\n" + codes[ch] + "\n")
            # Write data.
            fout.write(encoded_data)


def decode_fstr(file_in: str, file_out: str):
    """
    Decode file with name 'file_in' and
    write the result into file with name 'file_out'.
    Raise Exception if undefined signature of the file
    was found. That means it was not encoded with encode_fstr().
    """

    # For escape sequences.
    def decode_escape(ch: str):
        escape_dict = {
            "\\n": "\n",
            "\\t": "\t",
            "\\r": "\r",
            "\\\\": "\\",
            "\\0": "\0",
            '\\"': '"',
            "\\'": "'",
            "": " ",
        }
        return escape_dict.get(ch, ch)

    with open(file_in) as fin:
        if fin.readline() != "HC30\n":
            raise Exception("Undefined signature of the file.")
        # Read all the lines, the last line is the encoded data.
        lines = fin.readlines()
        codes = {}
        codes_count = len(lines[:-1])
        if codes_count % 2 != 0:
            raise Exception("File code table corruption.")

        i = 0
        while i < codes_count:
            # Remove quotes and newline, decode escape sequences.
            ch = decode_escape(lines[i][1:-2])
            code = lines[i + 1][:-1]

            codes[ch] = code
            i += 2

        decoded_data = decode(codes, lines[-1])
        with open(file_out, "w") as fout:
            fout.write(decoded_data)


if __name__ == "__main__":
    from sys import argv

    def print_info():
        print(f"Usage: {argv[0]} [flags] [input filename] [output filename]")
        print('Flags: "-a" / "-x" / "-h"')
        print('"-a" - to encode file and put the result into output file')
        print('"-x" - to decode file and put the result into output file')
        print('"-h" - to print help info')

    if len(argv) != 4 or argv[1] not in ("-a", "-x"):
        print_info()
        exit(1)
    try:
        if argv[1] == "-a":
            encode_fstr(argv[2], argv[3])
        else:
            decode_fstr(argv[2], argv[3])
    except Exception as err:
        print(err)
