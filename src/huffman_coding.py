from queue import PriorityQueue


def encode(msg: str) -> tuple[str, dict[str,str]]:
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

    class TrieNode:
        """Node for Trie"""

        def __init__(self):
            self.children = {}
            self.value = None

    class Trie:
        """Trie implementation for improving decoding efficiency."""

        def __init__(self):
            self.root = TrieNode()

        def insert(self, word: str, value):
            """
            Insert string into Trie and assign value to it.
            """
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.value = value

        def search_first(self, word: str):
            """
            Find the first occurrence of the string.
            Return (True, some_value) if found.
            Return (False, None) if not found.
            """
            node = self.root
            i = 0
            result_string = ""
            while not node.value:
                if i >= len(word):
                    return (False, None)
                ch = word[i]
                if ch not in node.children:
                    return (False, None)
                result_string += ch
                node = node.children[ch]
                i += 1
            return (node.value is not None, node.value)

    trie_codes = Trie()
    for code in codes:
        # Edge case.
        if code == "":
            continue
        trie_codes.insert(codes[code], code)

    output = ""
    i = 0
    while i < len(msg):
        is_found, decoded = trie_codes.search_first(msg[i:])
        if not is_found:
            raise TypeError("Undefined code. Failed to decode.")
        # Add decoded character and advance the iterator
        output += decoded
        i += len(codes[decoded])
    return output


def encode_f(file):
    pass


def decode_f(file):
    pass


# print(decode({"a": "000", "c": "01", "b": "10", "d": "11"}, "00100111"))
