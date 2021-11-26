str = 'ABBCCCCGGGGDEAAAEDBBBDFAGG'


class HuffmanNode:
    def __init__(self, freq, data, left, right):
        self.freq = freq
        self.data = data
        self.left = left
        self.right = right


def huffman_code(str):
    mapping = {}
    for character in str:
        if character not in mapping:
            mapping[character] = 1
        else:
            mapping[character] += 1

    generate_tree(mapping)
