str = 'ABBCCCCGGGGDEAAAEDBBBDFAGG'
char_binary_mapping = {}


class HuffmanNode:
    def __init__(self, freq, data, left, right):
        self.freq = freq
        self.data = data
        self.left = left
        self.right = right


def generate_tree(mapping):
    keyset = mapping.keys()
    priority_queue = []
    for key in keyset:
        node = HuffmanNode(mapping[key], key, None, None)
        priority_queue.append(node)
        priority_queue = sorted(priority_queue, key=lambda x: x.freq)
        while len(priority_queue) > 1:
            first = priority_queue.pop(0)
            second = priority_queue.pop(0)
            merge_node = HuffmanNode(first.freq + second.freq, '-', first, second)
            priority_queue.append(merge_node)
            priority_queue = sorted(priority_queue, key=lambda x: x.freq)
    return priority_queue.pop()


def set_binary_code(node, str):
    if node:
        if node.left is None and node.right is None:
            char_binary_mapping[node.data] = str
    # left
    if node.left:
        str += '0'
        set_binary_code(node.left, str)
        str = str[:-1]
    # right
    if node.right:
        str += '1'
        set_binary_code(node.right, str)
        str = str[:-1]


def huffman_code(str):
    mapping = {}
    for character in str:
        if character not in mapping:
            mapping[character] = 1
        else:
            mapping[character] += 1

    root = generate_tree(mapping)
    set_binary_code(root, '')
    for character in mapping:
        print('%-4r |%12s' % (character, char_binary_mapping[character]))

    s = ''

    for character in str:
        s += char_binary_mapping[character]
    return s


print(huffman_code(str))
