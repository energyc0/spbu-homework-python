from queue import PriorityQueue

class PriorityPair:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __lt__(self, other: 'PriorityPair'):
        return self.priority < other.priority

    # For debug purposes
    def __str__(self):
        return f"<!({self.priority})!, {self.value}>"
    # For debug purposes
    def __repr__(self):
        return f"<!({self.priority})!, {self.value}>"
    
def encode(s: str) -> tuple[str, dict]:
    # Count frequences of characters
    frequency = dict()
    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    print(len(frequency))
    if len(frequency) == 1:
        return tuple([len(s) * '0', (s[0], '0')])
    # Put frequences into priority queue
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
        #print(item)
        sorted_frequency.put(item)
    
    # Unwrap the characters and assign codes to them.
    #print(sorted_frequency.queue[0])
    codes = dict()
    if not sorted_frequency.empty():
        codes[sorted_frequency.queue[0]] = ''
    
    while not sorted_frequency.empty():
        item = sorted_frequency.get()
        code = codes[item]
        #print(code, item.value)
        if isinstance(item.value, str):
            codes.pop(item)
            codes[item.value] = code
            #print(item.value, code)
            continue

        left = item.value[0]
        right = item.value[1]
        codes.pop(item)

        codes[left] = code + '0'
        codes[right] = code + '1'
        sorted_frequency.put(left)
        sorted_frequency.put(right)
    
    output_string = ""
    for ch in s:
        output_string += codes[ch]
    return (output_string, codes)
    
def decode(codes: dict, s: str) -> str:
    pass

def encode_f(file):
    pass

def decode(file):
    pass

def test_encode(input: str):
    out = (encode(input))
    print(out)
    print(len(out[0]))

test_encode("aaaaabbbbcccddffeeee")
test_encode("aaa")
test_encode("ab")